# IMPORTS:
import os
import sys
import re
import time
import random
import json
import requests
from .Config import colors

###################
### Goobler 2022 ##
###################
# Scripts made by Eric #

# PURE CLASSES:

#class colors:
  #HEADER = '\033[95m'
  #OKBLUE = '\033[94m'
  #OKCYAN = '\033[96m'
  #OKGREEN = '\033[92m'
  #WARNING = '\033[93m'
  #FAIL = '\033[91m'
  #ENDC = '\033[0m'
  #BOLD = '\033[1m'
  #UNDERLINE = '\033[4m'

# PURE FUNCS:

def start(tkn):
  resp = requests.get("https://goobl2.ericplayzyt.repl.co/api/get_name_using_auth", {"auth": f"{tkn}"}).text
  print(f"Starting bot({resp})...")
  resp2 = requests.post("https://goobl2.ericplayzyt.repl.co/api/login/bot_account", {"auth": f"{tkn}"})
  print(colors.BOLD + resp + " has logged in." + colors.ENDC)

def Application(client_id=None, token=None):
  if token == None:
    print(colors._FAIL + colors._BOLD + colors._UNDERLINE + "[GooblerAPI] You cannot execute 'MakeApplication' without the positional arguments, token. Remember, the token is the admin password to your application.")