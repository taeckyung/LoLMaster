from LolMaster import league, summoner
from pandas import DataFrame
import schedule
import datetime
import argparse
import time
import os


base_dir = './'


def job():
	today = datetime.date.today().strftime("%Y%m%d")
	base = os.path.join(base_dir, today)

	if not os.path.exists(base):
		os.mkdir(base)

	challenger: DataFrame = league.get_league_challenger()
	challenger_users: DataFrame = summoner.get_summoner_by_summoner_id(challenger['summonerId'])
	challenger_users.to_csv(os.path.join(base, 'challenger.csv'))

	grandmaster: DataFrame = league.get_league_grandmaster()
	grandmaster_users: DataFrame = summoner.get_summoner_by_summoner_id(grandmaster['summonerId'])
	grandmaster_users.to_csv(os.path.join(base, 'grandmaster.csv'))

	master: DataFrame = league.get_league_master()
	master_users: DataFrame = summoner.get_summoner_by_summoner_id(master['summonerId'])
	master_users.to_csv(os.path.join(base, 'master.csv'))


def parse_args():
	parser = argparse.ArgumentParser()

	parser.add_argument('base_dir',
	                    help="Base directory to store data.")

	parser.add_argument('-t', '--time', default='23:45',
	                    help='Time to collect user data every day. Default is 23:45')

	parser.add_argument('-n', '--now', action='store_true',
	                    help="execute only once without scheduling")

	return parser.parse_args()


args = parse_args()
base_dir = args.base_dir

if args.now:
	job()
else:
	schedule.every().day.at(args.time).do(job)

	while True:
		schedule.run_pending()
		time.sleep(1)
