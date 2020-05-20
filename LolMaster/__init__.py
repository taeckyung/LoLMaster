from LolMaster.base import base
from LolMaster import config
import logging
import sys
import os

DEBUG = False

if not os.path.exists(base):
	os.mkdir(base)

logging.basicConfig(filename=os.path.join(base, 'log'), level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if DEBUG:
	root = logging.getLogger()
	handler = logging.StreamHandler(sys.stdout)
	handler.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler.setFormatter(formatter)
	root.addHandler(handler)

config.init()
