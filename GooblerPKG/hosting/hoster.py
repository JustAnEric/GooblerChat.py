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
  resp = requests.post('https://goobl2.ericplayzyt.repl.co/api/hosts/hostforever', {"auth": tkn})

def startHosting(tkn="AutoCreatedApplication"):
  resp = requests.post('https://goobl2.ericplayzyt.repl.co/api/hosts/start', {"auth": tkn})