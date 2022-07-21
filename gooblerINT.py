# IMPORTS:
import os
import sys
import re
import time
import random
import json
import requests
from .config.colors import Colour

###################
### Goobler 2022 ##
###################
# Scripts made by Eric #



# PURE FUNCS:

def start(tkn):
  resp = requests.get("https://goobler.imango.com.au/api/get_name_using_auth", {"auth": f"{tkn}"}).json()
  print(f"Starting {resp['user_name']}...")
  resp2 = requests.post("https://goobler.imango.com.au/api/login/bot_account", {"auth": f"{tkn}"}).json()
  print(resp['user_name'] + "has logged in.")

def Application(client_id=None, token=None):
  if token == None:
    print(Colour.FAIL + Colour.BOLD + Colour.UNDERLINE + "[GooblerAPI] You cannot execute 'MakeApplication' without the positional arguments, token. Remember, the token is the admin password to your application.")