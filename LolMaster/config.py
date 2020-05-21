from LolMaster.error import KeyNotSetError, RegionNotSetError
from configparser import ConfigParser
import logging
import sys
import os


base = os.path.expanduser('~/.lolMaster')
if not os.path.exists(base):
	os.mkdir(base)

logging.basicConfig(filename=os.path.join(base, 'log'), level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

root = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.NOTSET)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

fileName = os.path.join(base, 'config')
config = ConfigParser()

if not os.path.exists(fileName):
	with open(fileName, 'w+'):
		pass

config.read(fileName)
if not config.has_section('main'):
	config.add_section('main')


def set_key(key: str):
	config.set('main', 'key', key)
	with open(fileName, 'w+') as fp:
		config.write(fp)


def get_key() -> str:
	config.read(fileName)
	if config.has_option('main', 'key'):
		return config.get('main', 'key')
	else:
		raise KeyNotSetError("You should set key by config.store_key().")


def set_region(region: str):
	config.set('main', 'region', region.lower())
	with open(fileName, 'w+') as fp:
		config.write(fp)


def get_region() -> str:
	config.read(fileName)
	if config.has_option('main', 'region'):
		return config.get('main', 'region')
	else:
		raise RegionNotSetError("You should set region by config.store_region().")


def set_verbose(level: int):
	config.set('main', 'verbose', str(level))
	with open(fileName, 'w+') as fp:
		config.write(fp)


def get_verbose() -> int:
	config.read(fileName)
	if config.has_option('main', 'verbose'):
		level = int(config.get('main', 'verbose'))
		if level <= 0:
			return logging.NOTSET
		elif level == 1:
			return logging.ERROR
		elif level == 2:
			return logging.WARNING
		else:
			return logging.INFO
	else:
		return logging.NOTSET
