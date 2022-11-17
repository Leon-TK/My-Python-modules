import os, stat, sys, datetime
from ast import Index
from io import FileIO, TextIOWrapper
from string import Template

from .stringFormat import *
from . import constants

#TODO: add file extention filter

#Function argument, what to replace
_LICENSE = 0
_COPYRIGHT = 1

#replaces only first match
def _replace(filePath, newData, t):
    with open(filePath, "r+", encoding="utf-8") as file:
        fileData = file.readlines()
        file.seek(0)
        lineIndex = 0
        beginString = constants.SPDX_LICENCE if t == _LICENSE else constants.SPDX_COPYRIGHT
        for line in fileData:
            licenseIndex = line.find(beginString)
            if licenseIndex > -1:
                newLine = line[:licenseIndex] # Remains chars before old licence
                newLine += f"{beginString} {newData}\n"
                fileData[lineIndex] = newLine
                #FUTURE If you need to process multiple SPDX you should move them after loop but it causes perf. drop
                file.seek(0)
                file.truncate() #TODO: make backup
                file.writelines(fileData)
                break
            lineIndex += 1
        """ try:
            fileData = _replaceFisrtMatch(fileData, f"{beginString} {newData}\n", t)
        except UserWarning:
            print(f"Cant find {beginString}") """

def _replaceFisrtMatch(linesList, newData, t) -> list:
    beginString = constants.SPDX_LICENCE if t == _LICENSE else constants.SPDX_COPYRIGHT
    lineIndex = 0
    for line in linesList:
        #TODO: if you use convention, that is copyright and licence is written at the begining, you dont need to loop over all lines
            findIndex = line.find(beginString)
            if findIndex > -1:
                linesList[lineIndex] = f"{newData}"
                return linesList
            lineIndex += 1
    #It's here because "None" check in the caller will lead to copy old data again for restore
    raise UserWarning

#replaces only first match
def replaceLicense(filePath, newLicense):
    _replace(filePath, newLicense, _LICENSE)

#replaces only first match
#TODO: this is same as replaceCopyrightInDirectory() DRY
def replaceLicenseInDirectory(path, extentions, newCopyright, bRecursive):
    for root, nestedDirs, fileNames in os.walk(path):
        for file in fileNames:
            try:
                dotDelimited = file.split('.')
                ext = dotDelimited[len(dotDelimited) - 1]
            except IndexError: # pass files with no extentions
                continue
            
            if ext in extentions:
                _replace(os.path.join(root, file), newCopyright, _LICENSE)
        if not bRecursive: break

#TODO option for setting auto year date
#TODO detailed options for copyright, e.g. holder, email
#replaces only first match
def replaceCopyright(filePath, newCopyright):
    _replace(filePath, newCopyright, _COPYRIGHT)

#replaces only first match
def replaceCopyrightInDirectory(path, extentions, newCopyright, bRecursive):
    for root, nestedDirs, fileNames in os.walk(path):
        for file in fileNames:
            try:
                dotDelimited = file.split('.')
                ext = dotDelimited[len(dotDelimited) - 1]
            except IndexError: # pass files with no extentions
                continue
            
            if ext in extentions:
                _replace(os.path.join(root, file), newCopyright, _COPYRIGHT)
        if not bRecursive: break