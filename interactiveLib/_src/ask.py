import sys

from . import utils
from . import constants

__all__ = ["askPath", "askYesNo", "askList", "askInt", "askStr"]

def askPath(path: str, msg: str = constants.ASK_PATH_MSG, bFile: bool = False) -> str | None:
    print(msg)
    inpt = utils.getInputLine()
    #TODO: check path with my library
    if bFile:
        if not utils.isFile(inpt):
            print("File path is required")
            return None
    return utils.fixPath(inpt)
    
def askYesNo(msg: str = constants.ASK_YES_MSG) -> bool:
    print(msg + constants.ASK_YES_NOTE)
    inpt = utils.getInputLine()
    if inpt == "Y" or inpt == "yes":
        return True
    elif inpt == "n" or inpt == "no":
            return False

def askList(msg: str = constants.ASK_LIST_MSG, delimiter: str = ' ') -> list:
    print(msg)
    inpt = utils.getInputLine()
    return utils.parseAsList(inpt, delimiter)

def askInt(msg: str = constants.ASK_INT_MSG) -> int:
    print(msg)
    inpt = utils.getInputLine()
    return int(inpt)
def askStr(msg: str):
    print(msg)
    inpt = utils.getInputLine()
    return inpt
