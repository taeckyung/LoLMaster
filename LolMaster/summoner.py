from typing import Union
from LolMaster.api import RiotURL
from pandas import Series, DataFrame, json_normalize


def get_summoner_by_summoner_id(summoner_ids: Union[str, Series]):
	if type(summoner_ids) == str:
		summoner_ids = Series(summoner_ids)

	df = DataFrame()
	for account_id in summoner_ids:
		url = "/lol/summoner/v4/summoners/" + format(account_id)
		res = RiotURL(url).request()
		if res is not None:
			df = df.append(json_normalize(res))

	return df
