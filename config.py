from LolMaster import config
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-k', '--key', required=True,
                    help='api key')

parser.add_argument('-r', '--region', required=True,
                    help='region')

args = parser.parse_args()

config.set_key(args.key)
config.set_region(args.region)
