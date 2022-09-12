import requests
#from config import colors

###################
### Goobler 2022 ##
###################
# Scripts made by Eric #


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def hostForever(bool=False, tkn=None):
    if tkn != None:
        resp = requests.post('https://goobler.imango.com.au/api/hosts/hostforever', {"auth": tkn})
    else:
        print(colors.WARNING + colors.BOLD + colors.UNDERLINE + "[GooblerAPI] You cannot run hostForever without a token! Remember, the token is the admin password to your application.")

def startHosting(tkn=None):
  if tkn != None:
    resp = requests.post('https://goobler.imango.com.au/api/hosts/start', {"auth": tkn})
  else:
    print(colors.WARNING + colors.BOLD + colors.UNDERLINE + "[GooblerAPI] You cannot run hostForever without a token! Remember, the token is the admin password to your application.")