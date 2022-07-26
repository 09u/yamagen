import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = BASE_DIR + '/../config/config.json'

with open(CONFIG_PATH, 'r') as f:
    CONFIGS = json.load(f)

# The domain name 
domains = CONFIGS["domain"]
local_parts = CONFIGS["local-part"]
