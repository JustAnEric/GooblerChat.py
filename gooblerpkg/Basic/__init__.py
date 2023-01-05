###################
### Goobler 2023 ##
###################
# Scripts made by Eric #

import requests

print("[Process] INITIALIZED")

class ctx: 
    def __init__(self):
        pass

    def send_message(self, message):
        resp = requests.get("https://goobl2.ericplayzyt.repl.co/api/messaging/send_message/")

def command(function, **kwargs):
    return function and ctx