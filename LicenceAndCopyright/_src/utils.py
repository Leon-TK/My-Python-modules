from . import constants

def _isCopyrightExist(fileLines):
    for line in fileLines:
        if constants.SPDX_COPYRIGHT in line:
            return True
        else: continue
    return False

def _isLicenceExist(fileLines):
    for line in fileLines:
        if constants.SPDX_LICENCE in line:
            return True
        else: continue
    return False
def _findLicenceSignatureIndexIn(line, licenceSignature):
    pass
def pasteLineToBeginOfFileData(fileData: list, line):
    return [line] + fileData
    
#TODO: multiline comment
def getCommentCharsByExtention(extention):
    if extention in constants.PY_EXT:
        return "#"
    if extention in constants.CPP_EXTS + constants.SHARP_EXT:
        return "//"