from ntpath import join
import os
from pathlib import Path

import fileExtentionsConstants as fileExtentions

from . import regexFactory
from . import constants
from .conventions.convention import SinglelineTodoConvention
from .settings import CmdLineSettings

# returns list of files with given extention
# generator
def getFilteredListOfFiles(directory, extentions: list):
    for rootDir, dirs, names in os.walk(directory):
        for name in names:
            ext = os.path.splitext(name)[-1].lstrip('.')
            if ext in extentions:
                yield os.path.join(rootDir, name), ext

def getSinglelineRegexBy(extention: str, convention: SinglelineTodoConvention):
    if extention in fileExtentions.CPP_EXTS or extention in fileExtentions.SHARP_EXTS:
        return regexFactory.CRegexFactory(convention).get()
    elif extention in fileExtentions.PY_EXTS:
        return regexFactory.PythonRegexFactory(convention).get()
    elif extention in fileExtentions.PLAINTEXT_EXTS:
        return regexFactory.PlainRegexFactory(convention).get()
    return None


def clearFile(file):
    file.seek(0)
    file.truncate()

def getDefaultNamedOutputPathFrom(dirPath):
    return joinDirWithFileName(dirPath, constants.DEFAULT_OUTPUT_NAME)

def joinDirWithFileName(dirPath, fileName):
    return Path.joinpath(Path(dirPath), Path(fileName))

# if -n is set, set new output path
# outputPath of cmd settings can have fileName, what to do?
class OutputFilePathResolver:
    def __init__(self, cmdLineSettings: CmdLineSettings) -> None:
        self._cmdLineSettings = cmdLineSettings

    def handleSameDirForOutput(self):
        if self._cmdLineSettings.outputName is not None:
            return joinDirWithFileName(self._cmdLineSettings.srcPath, self._cmdLineSettings.outputName)
        else:
            return getDefaultNamedOutputPathFrom(self._cmdLineSettings.srcPath)

    def handleNotSameDirForOutput(self):
        if self._cmdLineSettings.outputName is not None: 
            return joinDirWithFileName(self._cmdLineSettings.outputPath, self._cmdLineSettings.outputName)
        else:
            getDefaultNamedOutputPathFrom(self._cmdLineSettings.outputPath)
            
    def resolvePath(self) -> Path:
        if self._cmdLineSettings.bSameDirForOutput:
            self.handleSameDirForOutput()
        else:
            self.handleNotSameDirForOutput()
