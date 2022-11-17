import sys

import interactiveLib as interactive

from ..interface import *

#TODO: sort all fucntions into some modules
def prepareInput(inputStr: str):
    if inputStr.endswith('\n'):
        inputStr = inputStr[:-1] # remove \n
    inputStr = inputStr.strip()
    return inputStr
def checkYesOrNo(str):
    str = prepareInput(str)
    if str == "Y" or str == "yes":
        return True
    elif str == "n" or str == "no":
        return False
def parseAsList(str):
    return str.split()
def checkDirectoryPath(path):
    while isFile(path):
        print("Error: use directory, not file path")
        path = askPath()
    return path
def fixPath(path):
    return path.replace('\\', "\\")
def isFile(path):
    last = path.split("\\").pop()
    return len(last.split('.')) > 1
def askRecursiveWalk() -> bool:
    print("Do recursive walk into folders? [Y]yes/[n]no :")
    for line in sys.stdin:
        return checkYesOrNo(line)
def askPath():
    print("Enter file or directory path:")
    for line in sys.stdin:
        line = prepareInput(line)
        return line.replace('\\', "\\")
def askOverwrite():
    print("Do overwrite existance entries? [Y]yes/[n]no :")
    for line in sys.stdin:
        return checkYesOrNo(line)
def askExtentions():
    print("List file extentions with whitespace without dot:")
    for line in sys.stdin:
        return parseAsList(prepareInput(line))
def askCopyright():
    print("Enter your copyright entry:")
    for line in sys.stdin:
        return prepareInput(line)
def askLicence():
    print("Enter your licence entry:")
    for line in sys.stdin:
        return prepareInput(line)

def beginInteractiveMode():
    holder = interactive.askStr("Enter holder:")
    print("Enter holder:")
    for line in sys.stdin:
        holder = prepareInput(line)
        break
    print("Enter email:")
    for line in sys.stdin:
        email = prepareInput(line)
        break
    print("Enter licence:")
    for line in sys.stdin:
        licence = prepareInput(line)
        break
    path = askPath()
    print("Choose what to do - 1. Paste copyright and licence in directory's files\n\
        2. Replace copyright in directory's files\n\
        3. Replace licence in directory's files\n\
        4. Delete copyright and licence in directory's files")
    for line in sys.stdin:
        action = int(line)
        break
    if action == 1: #TODO: and path is directory, not file
        bOverwrite = askOverwrite()
        bRecursive = askRecursiveWalk()
        path = checkDirectoryPath(path)
        pasteAllInDirectory(path, holder, email, licence, bOverwrite, bRecursive)
    if action == 2:
        extentions = askExtentions()
        copyright = askCopyright()
        bRecursive = askRecursiveWalk()
        path = checkDirectoryPath(path)
        replaceCopyrightInDirectory(path, extentions, copyright, bRecursive)
    if action == 3:
        extentions = askExtentions()
        licence = askLicence()
        bRecursive = askRecursiveWalk()
        path = checkDirectoryPath(path)
        replaceLicenseInDirectory(path, extentions, licence, bRecursive)
    if action == 4:
        extentions = askExtentions()
        path = checkDirectoryPath(path)
        deleteAllInDirectory(path, extentions)
    sys.exit(0)


def beginCmdLineMode(): #TODO: implement this -  beginCmdLineMode
    try:
        holder = prepareInput(sys.argv[1])
    except IndexError:
        print("Error. Missing 1 argument - holder or -interactive")
        sys.exit(0)

    try:
        email = prepareInput(sys.argv[2])
    except IndexError:
        print("Error. Missing 2 argument - email")
        sys.exit(0)

    try:
        licenseUsed = prepareInput(sys.argv[3])
    except IndexError:
        print("Error. Missing 3 argument - license is used")
        sys.exit(0)
    
    try:
        path = prepareInput(sys.argv[4])
    except IndexError:
        print("Error. Missing 4 argument - path")
        sys.exit(0)

    try:
        action = int(prepareInput(sys.argv[5]))
    except IndexError:
        print("Error. Missing 5 argument - action")
        sys.exit(0)