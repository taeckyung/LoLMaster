from LolMaster.error import KeyNotSetError, RegionNotSetError
from LolMaster.base import base
from configparser import ConfigParser
import os

config = ConfigParser()
fileName = os.path.join(base, 'config')


def init():
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


def get_key():
	if config.has_option('main', 'key'):
		return config.get('main', 'key')
	else:
		raise KeyNotSetError("You should set key by config.store_key().")


def set_region(region: str):
	config.set('main', 'region', region.lower())
	with open(fileName, 'w+') as fp:
		config.write(fp)


def get_region():
	if config.has_option('main', 'region'):
		return config.get('main', 'region')
	else:
		raise RegionNotSetError("You should set region by config.store_region().")
