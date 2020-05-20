# LolMaster

LolMaster is a tool to collect rank game data from League of Legends.

## Requirements

Python version >= 3.5

```pip install pandas schedule requests```

## Configuration

You should initialize your API key and the target region by:

```python config.py -k KEY -r REGION```

---

You can also set API key and region by importing ```LolMaster.config```.

```Python
from LolMaster import config
config.set_key('RGAPI-...')
config.set_region('kr')
```

##