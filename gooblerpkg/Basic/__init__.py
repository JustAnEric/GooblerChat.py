###################
### Goobler 2023 ##
###################
# Scripts made by Eric #

print("[Process] INITIALIZED")

class ctx: 
    def __init__(self):
        pass

def command(function, **kwargs):
    commandname = function.__name__()
    function()
    return 