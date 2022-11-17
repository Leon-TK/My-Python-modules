import os, stat, sys, datetime
from ast import Index
from io import FileIO, TextIOWrapper
from string import Template

from ._shortcut.license import *
from ._shortcut.copyright import *
from . import stringFormat
from . import replace
from . import constants
from . import utils

#TODO: what to do if different order of copy and licence?

def _retriveFileCreationYear(filePath) -> str:
    #FUTURE on unix ST_CTIME may not be as creation time(?)
    return datetime.datetime.utcfromtimestamp(os.stat(filePath)[stat.ST_CTIME]).strftime("%Y")

def prepareCopyrightLine(holder, email, commentChars, bNewLine, year = '') -> str:
    copyrightTextTemplate = Template(f"{constants.SPDX_COPYRIGHT} (c) $fileYear {holder} {email}")
    copyrightt = None

    if len(year) > -1: copyrightt = copyrightTextTemplate.substitute(fileYear=year)
    else: copyrightt = f"{constants.SPDX_COPYRIGHT} (c) {holder} {email}"

    if bNewLine: copyrightt += '\n'
    return commentChars + copyrightt

def prepareLicenceLine(commentChars, licenseType, bNewLine) -> str:
    licenseShortcut: LicenseShortcut = SpdxLicenseShortcut(licenseType) #TODO rename lisencetemplate to license shortcut and all classes even copyright
    licenseText = licenseShortcut.getStr()

    if bNewLine: licenseText += '\n'

    return commentChars + licenseText

def pasteCopyrightAndLicence(file: TextIOWrapper, holder, email, commentChars, bNewLine, licenseType, year = '', bOverwrite = False) -> bool:
    copyrightLine = prepareCopyrightLine(holder, email, commentChars, bNewLine, year)
    licenceLine = prepareLicenceLine(commentChars, licenseType, bNewLine)
    fileData = file.readlines()

    bCopyrightExist = utils._isCopyrightExist(fileData)
    bLicenceExist = utils._isLicenceExist(fileData)

    if not bOverwrite:
        if bCopyrightExist and bLicenceExist:
            file.close()
            return False
        else:
            if bCopyrightExist or bLicenceExist:
                #Partitial signature is not allowed
                raise UserWarning
            fileData = utils.pasteLineToBeginOfFileData(fileData, licenceLine)
            fileData = utils.pasteLineToBeginOfFileData(fileData, copyrightLine)     
    else:
        #Reverse order of licence-copyright
        if bLicenceExist:
            try:
                fileData = replace._replaceFisrtMatch(fileData, licenceLine, replace._LICENSE)
            except UserWarning: 
                print("Cant find licence, that's already founded with bLicenceExist")
                sys.exit(1)
        else:
            fileData = utils.pasteLineToBeginOfFileData(fileData, licenceLine)
        if bCopyrightExist:
            try:
                fileData = replace._replaceFisrtMatch(fileData, copyrightLine, replace._COPYRIGHT)
            except UserWarning:
                print("Cant find copyright, that's already founded with bCopyrightExist")
                sys.exit(1)
        else:
            fileData = utils.pasteLineToBeginOfFileData(fileData, copyrightLine)
    file.seek(0)
    file.truncate() #TODO: make backup
    file.writelines(fileData)
    return True

#date of copyright is setted to file creation  date
def pasteCopyAndLicenseInDirectory(path, holder, email, license, bOverwrite = False, bRecursive = False):
    #TODO: add extentions as argument
    
    def processFile(commentChars) -> bool:
        with open(filePath, "r+", encoding="utf-8") as file:
            try:
                result = pasteCopyrightAndLicence(file, holder, email, commentChars, True, license, _retriveFileCreationYear(filePath), bOverwrite)
            except UserWarning:
                print(f"Warning! Partitial signature - either copyright or licence is missing. Skipping file {filePath}\n")
                file.close()
            #handle result
            file.close()
    
    for root, nestedDirs, fileNames in os.walk(path):
        for fileName in fileNames:
            try:
                filePieces = fileName.split(".")
                fileExt = filePieces[len(filePieces) - 1] # get chars after last "." of file name
            except IndexError: # pass files with no extentions
                continue

            filePath = os.path.join(root, fileName)

            if fileExt in constants.CPP_EXTS + constants.SHARP_EXT:
                processFile(constants.C_COMMENT_CHAR)
                continue

            if fileExt in constants.PY_EXT:
                processFile(constants.PY_COMMENT_CHAR)
                continue

        if not bRecursive: break