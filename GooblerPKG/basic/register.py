import os

###################
### Goobler 2022 ##
###################
# Scripts made by Eric #


def RegisterCommands(dir="./GooblerPKG/basic/commands/"):
  for each in os.listdir(dir):
    if each.endswith('.py'):
      print("\n Registered command "+str(each))