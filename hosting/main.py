from distutils.log import warn
import requests

def hostForever(bool=False, tkn=None):
    if tkn != None:
        resp = requests.post('https://goobler.imango.com.au/api/hosts/hostforever', {"auth": tkn})
    else:
        warn("[GooblerAPI] You cannot run hostForever without a token! Remember, the token is the admin password to your application.")