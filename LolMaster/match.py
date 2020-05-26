from typing import Union, List
from LolMaster.api import RiotURL
from pandas import Series, DataFrame, json_normalize


def get_list_by_account(account_ids: Union[str, Series],
		champion_ids: Union[None, List[int]] = None,
		queue_ids: Union[None, List[int]] = None,
		seasons: Union[None, List[int]] = None,
		begin_time: Union[None, int] = None,
		end_time: Union[None, int] = None):
	if champion_ids is None:
		champion_ids = []
	if queue_ids is None:
		queue_ids = []
	if seasons is None:
		seasons = []

	if type(account_ids) == str:
		account_ids = Series(account_ids)

	df = DataFrame()
	for account_id in account_ids:
		url = RiotURL('/lol/match/v4/matchlists/by-account/' + format(account_id))
		url.set_query('champion', champion_ids) \
			.set_query('queue', queue_ids) \
			.set_query('season', seasons)
		if begin_time is not None:
			url.set_query('beginTime', str(begin_time))
		if end_time is not None:
			url.set_query('endTime', str(end_time))
		res = url.request()

		if res is not None:
			df = df.append(json_normalize(res['matches']))

	return df


def get_match_by_match_id(match_ids: Union[str, Series]):
	if type(match_ids) == str:
		match_ids = Series(match_ids)

	match_ids.drop_duplicates(inplace=True)

	df = DataFrame()
	for match_id in match_ids:
		url = RiotURL('/lol/match/v4/matches/' + format(match_id))
		res = url.request()

		if res is not None:
			df = df.append(json_normalize(res))
	return df
