from pathlib import Path

from . import core
from . import constants

def retrieveErrorStrings(bBeginingOfPath = False) -> bool:
    if bBeginingOfPath:
        excludeChars = constants.WIN_EXCLUDE_CHARS2_B
    else:
        excludeChars = constants.WIN_EXCLUDE_CHARS2

    return excludeChars + constants.WIN_EXCLUDE_STRINGS + constants.WIN_EXCLUDE_CHARS1

def directoryPathCheck(path: str):
    if len(path) > constants.WIN_PATH_MAX_LEN: return False

    parts = path.split(constants.WIN_PATH_DELIMITER)
    count = 0
    errorStrings = retrieveErrorStrings(False)
    for part in parts:
        if count == 0:
            if not core._fileNameCheck(part, constants.WIN_FILE_MAX_LEN, retrieveErrorStrings(True)): return False
        if not core._fileNameCheck(part, constants.WIN_FILE_MAX_LEN, errorStrings): return False
        count += 1
    return True

def fileNameCheck(name):
    return core._fileNameCheck(name, constants.WIN_FILE_MAX_LEN, retrieveErrorStrings(False))

def directoryNameCheck(name):
    return fileNameCheck(name)