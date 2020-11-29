import requests
import hashlib
from pprint import pprint
import dotenv
import os
import random_user_agent
from random_user_agent import user_agent
from aternos_api.account import Account

dotenv.load_dotenv()

# session = requests.session()

USERNAME = os.getenv('USR')
TOKEN = os.getenv('DISCORD_TOKEN')

# AGENT = user_agent.UserAgent(
# 	software_names=['chrome'],
# 	operating_systems=['windows', 'linux']
# 	).get_random_user_agent()

PASSWORD = os.getenv('PASS')

a = Account()
a.login(USERNAME, PASSWORD)
a.fetch_servers()
print(a.servers)

a.close()