from li import listarray

###################
### Goobler 2022 ##
###################
# Scripts made by Eric #


class ListValueType:
    def __init__(self, value):
        pass
    String = str()
    Integer = int()

def get_list():
    return listarray

class ListValues:
    def change_value(id, value:ListValueType):
        for item in listarray:
            if id == item:
                item[id] = value