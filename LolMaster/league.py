from pandas import json_normalize, DataFrame
from LolMaster.api import RiotURL


def get_league_grandmaster(queue: str = 'RANKED_SOLO_5x5'):
	return high_elo_wrapper("/lol/league/v4/grandmasterleagues/by-queue/%s", queue)


def get_league_master(queue: str = 'RANKED_SOLO_5x5'):
	return high_elo_wrapper("/lol/league/v4/masterleagues/by-queue/%s", queue)


def get_league_challenger(queue: str = 'RANKED_SOLO_5x5'):
	return high_elo_wrapper("/lol/league/v4/challengerleagues/by-queue/%s", queue)


def high_elo_wrapper(url: str, queue: str):
	res = RiotURL(url % queue).request()
	if res is None:
		return DataFrame()
	df = json_normalize(res['entries'])
	df = df.sort_values('leaguePoints', ascending=False)
	return df
