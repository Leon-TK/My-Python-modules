from asyncio import constants
from pathlib import Path

def bExceedsMaxLenght(name, maxLenght) -> bool:
    return len (name) > maxLenght
def bMissesExtention(name) -> bool:
    return len(Path(name).suffixes) == 0
def bConstainsElementFrom(container, object):
    for element in container:
        if element in object:
            return True
    return False
def bPathHasNavigatingChars(path) -> bool:
    if path.startswith(constants.D_DOT):
            if len(path) > len(constants.D_DOT): #separated 'if' statement for not checking ".." again in next 'elif'
                return True
            return False
    elif path.startswith(constants.DOT) and len(path) > len(constants.DOT):
        return True
    return False

def _fileNameCheck(name, maxLenght, errorStrings: list) -> bool:
    if bExceedsMaxLenght(name, maxLenght): return False
    if bConstainsElementFrom(errorStrings, name): return False
    if name.endswith(constants.DOT): return False
    return True