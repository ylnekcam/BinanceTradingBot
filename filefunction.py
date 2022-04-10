import json


def getPathFromJson(jsonpath):

  with open(jsonpath, 'r') as f:
    pathDict = json.load(f)
    return pathDict


def writeTxt(path,txt):
    with open(path, 'a') as f:
        return f.writelines(txt +'\n')