import requests
from .config.colors import Colour

def hostForever(bool=False, tkn=None):
    if tkn != None:
        resp = requests.post('https://goobler.imango.com.au/api/hosts/hostforever', {"auth": tkn})
    else:
        print(Colour.WARNING + Colour.BOLD + Colour.UNDERLINE + "[GooblerAPI] You cannot run hostForever without a token! Remember, the token is the admin password to your application.")

def startHosting(tkn=None):
  if tkn != None:
    resp = requests.post('https://goobler.imango.com.au/api/hosts/start', {"auth": tkn})
  else:
    print(Colour.WARNING + Colour.BOLD + Colour.UNDERLINE + "[GooblerAPI] You cannot run hostForever without a token! Remember, the token is the admin password to your application.")