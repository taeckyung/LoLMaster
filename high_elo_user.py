from LolMaster import league, summoner, match
from pandas import DataFrame
import pandas as pd
import schedule
import datetime
import argparse
import time
import os


summoner_dir = './'
match_dir = './'


def job():
	yesterday = datetime.datetime.now() - datetime.timedelta(1)
	base = os.path.join(summoner_dir, yesterday.strftime("%Y%m%d"))

	if not os.path.exists(base):
		os.mkdir(base)

	challenger: DataFrame = league.get_summoner_challenger()
	challenger_users: DataFrame = summoner.get_summoner_by_summoner_id(challenger['summonerId'])
	challenger_users.to_csv(os.path.join(base, 'challenger.csv'))

	grandmaster: DataFrame = league.get_summoner_grandmaster()
	grandmaster_users: DataFrame = summoner.get_summoner_by_summoner_id(grandmaster['summonerId'])
	grandmaster_users.to_csv(os.path.join(base, 'grandmaster.csv'))

	master: DataFrame = league.get_summoner_master()
	master_users: DataFrame = summoner.get_summoner_by_summoner_id(master['summonerId'])
	master_users.to_csv(os.path.join(base, 'master.csv'))

	base = os.path.join(match_dir, yesterday.strftime("%Y%m%d"))

	if not os.path.exists(base):
		os.mkdir(base)

	high_elo_users = pd.concat([master_users, grandmaster_users, challenger_users])
	print(high_elo_users)

	begin = int(1000 * yesterday.replace(hour=0, minute=0, second=0, microsecond=0).timestamp())
	end = int(1000 * yesterday.replace(hour=23, minute=59, second=59, microsecond=9999).timestamp())

	match_ids = match.get_list_by_account(high_elo_users['accountId'], begin_time=begin, end_time=end)
	print(match_ids)
	matches = match.get_match_by_match_id(match_ids['gameId'])
	print(matches)
	matches.to_csv(os.path.join(base, 'over_master.csv'))


def parse_args():
	parser = argparse.ArgumentParser()

	parser.add_argument('-s', '--summoner_dir', required=True,
	                    help="Base directory to store summoner data.")

	parser.add_argument('-m', '--match_dir', required=True,
	                    help="Base directory to store match data.")

	parser.add_argument('-t', '--time', default='00:00',
	                    help='Time to collect user data every day. Default is 00:00')

	parser.add_argument('-n', '--now', action='store_true',
	                    help="execute only once without scheduling")

	return parser.parse_args()


args = parse_args()
summoner_dir = args.summoner_dir
match_dir = args.match_dir

if args.now:
	job()
else:
	schedule.every().day.at(args.time).do(job)

	while True:
		schedule.run_pending()
		time.sleep(1)
