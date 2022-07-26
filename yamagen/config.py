import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = BASE_DIR + '/../config/config.json'


with open(CONFIG_PATH, 'r') as f:
    CONFIGS = json.load(f)



# The domain name 
DOMAINS = CONFIGS["domain"]
LOCAL_PARTS = CONFIGS["local-part"]
CONFIG_OUTPUT = CONFIGS["output"]
