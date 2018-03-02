from collections import OrderedDict

def remove_duplicates(inputstr):
    return "".join(OrderedDict.fromkeys(inputstr))