from LolMaster.base import base
from LolMaster import config
import logging
import os

if not os.path.exists(base):
	os.mkdir(base)

logging.basicConfig(filename=os.path.join(base, 'log'), level=logging.INFO,
                    format='%(asctime)s %(message)s')
config.init()
