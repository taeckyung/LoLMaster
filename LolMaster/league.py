from pandas import json_normalize, DataFrame
from LolMaster.api import RiotURL


def get_summoner_master(queue: str = 'RANKED_SOLO_5x5') -> DataFrame:
	return high_elo_wrapper("master", queue)


def get_summoner_grandmaster(queue: str = 'RANKED_SOLO_5x5') -> DataFrame:
	return high_elo_wrapper("grandmaster", queue)


def get_summoner_challenger(queue: str = 'RANKED_SOLO_5x5') -> DataFrame:
	return high_elo_wrapper("challenger", queue)


def high_elo_wrapper(tier: str, queue: str) -> DataFrame:
	url = "/lol/league/v4/%sleagues/by-queue/%s" % (tier, queue)
	res = RiotURL(url).request()
	if res is None:
		return DataFrame()
	df = json_normalize(res['entries'])
	df = df.sort_values('leaguePoints', ascending=False)
	return df
