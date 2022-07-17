from list import listarray

class ListValueType:
    def __init__(self, value):
        self.String = str(value)
        self.Integer = int(value)

def get_list():
    return listarray

class ListValues:
    def change_value(id, value:ListValueType):
        for item in listarray:
            if id == item:
                item[id] = value