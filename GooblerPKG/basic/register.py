import os

###################
### Goobler 2022 ##
###################
# Scripts made by Eric #


def RegisterCommands(dir="./GooblerPKG/basic/commands/"):
  try:
    if os.listdir(dir): pass
  except:
    os.mkdir(dir)
    with open(f'{dir}/Information', 'w') as f:
      f.write('For each command you need to add, make a new .py file inside the parent directory.')

  for each in os.listdir(dir):
    if each.endswith('.py'):
      print("\n Registered command "+str(each))