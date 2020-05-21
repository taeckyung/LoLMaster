from pandas import json_normalize, DataFrame
from LolMaster.api import RiotURL


def high_elo_wrapper(tier: str, queue: str) -> DataFrame:
	url = "/lol/league/v4/%sleagues/by-queue/%s" % (tier, queue)
	res = RiotURL(url).request()
	if res is None:
		return DataFrame()
	df = json_normalize(res['entries'])
	df = df.sort_values('leaguePoints', ascending=False)
	return df


def get_summoner_master(queue: str = 'RANKED_SOLO_5x5') -> DataFrame:
	return high_elo_wrapper("master", queue)


def get_summoner_grandmaster(queue: str = 'RANKED_SOLO_5x5') -> DataFrame:
	return high_elo_wrapper("grandmaster", queue)


def get_summoner_challenger(queue: str = 'RANKED_SOLO_5x5') -> DataFrame:
	return high_elo_wrapper("challenger", queue)


def get_summoner_general(tier: str, division: int, queue: str = 'RANKED_SOLO_5x5') -> DataFrame:
	tier = tier.upper()
	assert(tier in ['IRON', 'BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND'])
	assert(division in range(1, 5))

	roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV'}
	url = RiotURL("/lol/league/v4/entries/%s/%s/%s" % (queue, tier, roman[division]))
	df = DataFrame()

	i = 1
	while True:
		res = url.set_query('page', str(i)).request()
		if res is None or len(res) == 0:
			break
		df = df.append(json_normalize(res))
		i += 1
	df = df.sort_values('leaguePoints', ascending=False)
	return df
