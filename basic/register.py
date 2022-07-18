import os

def RegisterCommands(dir="./GooblerPKG/basic/commands/"):
  for each in os.listdir(dir):
    if each.endswith('.py'):
      print("\n Registered command "+str(each))