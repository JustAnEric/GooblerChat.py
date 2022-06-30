# IMPORTS:
import os
import sys
import re
import time
import random
import json
import requests

# PURE FUNCS:

def start(tkn):
  resp = requests.get("https://goobler.imango.com.au/api/get_name_using_auth", {"auth": f"Bearer {tkn}"}).json()
  print(f"Starting {resp['user_name']}...")
  
