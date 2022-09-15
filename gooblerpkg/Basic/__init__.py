###################
### Goobler 2022 ##
###################
# Scripts made by Eric #

print("[Process] INITIALIZED")

def command(function, **kwargs):
    commandname = function.__name__()
    function()