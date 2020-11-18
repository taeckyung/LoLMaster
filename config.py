from api import config
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-k', '--key', type=str,
                    help='api key')

parser.add_argument('-r', '--region', type=str,
                    help='region')

parser.add_argument('-v', '--verbose', type=int, choices=range(0, 4),
                    help='verbose level from 0 to 3; higher one generates more output.')

args = parser.parse_args()

if args.key is not None:
    config.set_key(args.key)
if args.region is not None:
    config.set_region(args.region)
if args.verbose is not None:
    config.set_verbose(args.verbose)
