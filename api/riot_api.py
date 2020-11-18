from api.error import KeyNotValidError, NotReachableError
from api import config
from typing import Iterable, Union, Dict
import requests
import logging
import time


class RiotURL:
	def __init__(self, url: str):
		self.url = url
		self.queries = {}
		if self.url[0] == '/':
			self.url = RiotURL.absolute_url(self.url)

	@staticmethod
	def absolute_url(url: str) -> str:
		region = config.get_region()
		base = "https://%s.api.riotgames.com" % region
		return base + url

	def set_query(self, query_name: str, queries: Union[str, Iterable]) -> 'RiotURL':
		new_queries = []
		if type(queries) is str:
			new_queries = [queries]
		for query in queries:
			new_queries.append(str(query))
		self.queries[query_name] = new_queries
		return self

	def get_url_with_query(self) -> str:
		final_url = self.url
		first = True
		for query_name in self.queries.keys():
			if first:
				final_url += '?'
				first = False
			else:
				final_url += '&'
			final_url += "%s=%s" % (query_name, ','.join(self.queries[query_name]))
		return final_url

	def request(self, max_retry: int = 5) -> Union[None, Dict]:
		self.set_query('api_key', config.get_key())
		url = self.get_url_with_query()

		while max_retry > 0:
			r = requests.get(url)

			if r.status_code == 200:
				return r.json()
			elif r.status_code == 404:
				logging.warning("Data not found: %s" % url)
				return None
			elif r.status_code == 429:
				backoff = r.headers.get('Retry-After')
				if backoff is None:
					logging.warning("Code 429 with no Retry-After.")
					logging.warning(r.headers)
					backoff = 30
				backoff = int(backoff)
				logging.info("Backoff for %d seconds." % backoff)
				time.sleep(backoff)
				continue
			else:
				logging.error(url)
				logging.error(r.json().get('status'))

				if r.status_code == 401:
					logging.error("API token is not included.")
					raise NotReachableError
				elif r.status_code == 403:
					logging.error("API token or URL is not valid.")
					raise KeyNotValidError
				else:
					logging.error("Unknown error of code %d. Retrying." % r.status_code)
					max_retry -= 1
					continue

		return None
