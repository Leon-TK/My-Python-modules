import sys

def prepareInput(inputStr: str):
    if inputStr.endswith('\n'):
        inputStr = inputStr[:-1] # remove \n
    inputStr = inputStr.strip()
    return inputStr
    
def parseAsList(str, delimiter):

    return str.split(delimiter)
def fixPath(path):
    return path.replace('\\', "\\")

def isFile(path):
    last = path.split("\\").pop()
    return len(last.split('.')) > 1

def getInputLine():
    for line in sys.stdin:
        return prepareInput(line)