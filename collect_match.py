from LolMaster import match
import pandas as pd
import datetime
import os


today = datetime.date.today().strftime("%Y%m%d")
path = os.path.join('./data/summoner/', today)

master = pd.read_csv(os.path.join(path, 'master.csv'))
grandmaster = pd.read_csv(os.path.join(path, 'grandmaster.csv'))
challenger = pd.read_csv(os.path.join(path, 'challenger.csv'))

high_elo = pd.concat([master, grandmaster, challenger])

match_ids = match.get_list_by_account(high_elo['accountId'])
print(match_ids)
matches = match.get_match_by_match_id(match_ids)
print(matches)
matches.to_csv('./data/match/over_master.csv')