import re
import shutil
import os

from . import utils
from . import constants

#TODO: implement delete functions

def deleteCopyright(filePath):
    with open(filePath, "r+", encoding="utf-8") as file:
        fileData = file.readlines()
        if not utils._isCopyrightExist(fileData):
            print(f"No copyright in {file}")
            return
            
        lineIndex = 0
        extention = filePath.split(".").pop() #TODO: replace all other implementations with this approach
        regex = utils.getCommentCharsByExtention(extention) + r"[^\S\r\n]*"
        regex += constants.DEFAULT_COPYRIGHT
        regex += r"[^\S\r\n]*\s"
        for line in fileData:
            result = re.match(regex, line)
            if result is not None:
                break
            lineIndex += 1
        else: return
        fileData.pop(lineIndex)
        file.seek(0)
        file.truncate() #TODO: make backup
        file.writelines(fileData)
        
def deleteLicence(filePath):
    with open(filePath, "r+", encoding="utf-8") as file:
        fileData = file.readlines()
        if not utils._isLicenceExist(fileData):
            print(f"No licence in {file}")
            return
            
        lineIndex = 0
        extention = filePath.split(".").pop() #TODO: can return not what you want
        regex = utils.getCommentCharsByExtention(extention) + constants.DEFAULT_LICENCE
        regex += r"[^\S\r\n]*\s"
        for line in fileData:
            result = re.match(regex, line)
            if result is not None:
                break
            lineIndex += 1
        else: return
        fileData.pop(lineIndex)
        file.seek(0)
        file.truncate()
        file.writelines(fileData)

def deleteCopyrightAndLicene(file, extention):
    with open(file, "r+", encoding="utf-8") as file:
        fileData = file.readlines()
        if not utils._isCopyrightExist(fileData) and not utils._isLicenceExist(fileData):
            print(f"No copyright and licence in {file}")
            return

def deleteCopyrightAndLicenceInDirectory(path, extentions):
    for root, nestedDirs, fileNames in os.walk(path):
        for fileName in fileNames:
            fileExt = fileName.split(".").pop() #TODO: can return not what you want
            if fileExt in extentions:
                filePath = os.path.join(root, fileName)
                deleteCopyright(filePath)
                deleteLicence(filePath)
