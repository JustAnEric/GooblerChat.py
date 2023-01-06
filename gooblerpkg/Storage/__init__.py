###################
### Goobler 2022 ##
###################
# Scripts made by Eric #

commandsRegistered = {} #all commands that have been registered

def registerCommand(name, commandLogic):
    commandsRegistered[name] = commandLogic

def getCommand(name):
    return commandsRegistered[name]

def executeCommand(name, args):
    command = getCommand(name)
    if command:
        command(args)

registerCommand('help', help)