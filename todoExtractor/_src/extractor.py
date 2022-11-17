#SPDX-FileCopyrightText: 2022 Leonid Tkachenko leontkdev@gmail.com
#SPDX-License-Identifier: MIT License

import os
import re
import sys
from pathlib import Path

import fileExtentionsConstants as fileExtentions

from . import constants
from . import utils
from . import settings
from .settings import ExtractionSettings, OutputFileSettings, CmdLineSettings
from .conventions.leontk import LeontkConvention
from .conventions.universal import UniversalConvention

#TODO: extraction funcs cannot find TODOs in multiline comments
#TODO: can be situations when in output file could be duplicate todos. ProcessDstFileExisting preventes this, but things tend to change
#TODO: delete dst file if there no TODOs
#TODO: add ability to save output file in source folder with creation data note
#TODO: directory with no overwrie option appends to outputfile

def _terminateOnDstFileExistance(dstPath):
    #TODO: Throw exception?
    print(f"Output file already exists - {dstPath}\nUse another file name") # it's for safety
    sys.exit(0)

def _resolveDstFileOpenMode(bFromLoop, bOverwriteOutput) -> str:
    if bFromLoop:
        return 'a+'
    else:
        return 'a' if not bOverwriteOutput else 'a+'

def _getReadOpenFileMode() -> str:
    mode = 'r'
    assert(mode == 'r')
    return mode

def _processBuffer(buffer, regex, dstFile, srcPath):

    def processMatch(regexMatchResult, dstFile, lineCount, srcPath):

        def processTodo(todo, dstFile, lineCount, srcPath):
            if todo.endswith("\n"):
                todo = todo[:-1] #remove newline
            dstFile.write(f"TODO: {todo}, line - {lineCount + 1}, file - {srcPath}\n")
            dstFile.flush()

        findedTodos = regexMatchResult.string.split("TODO:")

        if len(findedTodos) >= 2:
            findedTodos = findedTodos[1:] #remove leftside of first split, cause we dont need it
            for todo in findedTodos:
                processTodo(todo, dstFile, lineCount, srcPath)
        else:
            todo = regexMatchResult.string
            processTodo(todo, dstFile, lineCount, srcPath)

    lineCount = 0
    for line in buffer:
        #TODO: what if multiline case?
        regexMatchResult = re.search(regex, line)
        #TODO: deal with that mess. this is because of universal regex
        if regexMatchResult is not None:
            processMatch(regexMatchResult, dstFile, lineCount, srcPath)
        lineCount += 1

def _extract(srcPath, dstPath, extractionSettings: ExtractionSettings):

    def proccesOutputExistance():
        if extractionSettings.bOverwriteOutput is not True and extractionSettings.bFromLoop is not True and os.path.exists(dstPath):
            _terminateOnDstFileExistance(dstPath)

    def getFileBuffer(srcFile):
        try:
            fileBuffer = srcFile.readlines()
        except UnicodeDecodeError:
            print(f"Unicode error in {srcPath}, passing...")
            return
        return fileBuffer

    proccesOutputExistance()

    with open(srcPath, _getReadOpenFileMode(), encoding="utf-8") as srcFile,\
         open(dstPath, _resolveDstFileOpenMode(extractionSettings.bFromLoop, extractionSettings.bOverwriteOutput), encoding="utf-8") as dstFile:

        fileBuffer = getFileBuffer(srcFile)

        if extractionSettings.bOverwriteOutput:
            utils.clearFile(dstFile)

        _processBuffer(fileBuffer, extractionSettings.regex, dstFile, srcPath)

def extractFromFile(cmdLineSettings: CmdLineSettings):
    
    def processNullExtention(extention):
        if extention is None or extention == '':
            raise Exception

    def prepareExtractionSettings(extractionSettings):
        extractionSettings.bOverwriteOutput = cmdLineSettings.bOverwriteOutput
        extractionSettings.bSameDirForOutput = cmdLineSettings.bSameDirForOutput
        extractionSettings.outputFileSettings.name = cmdLineSettings.outputName
        #TODO: refactor
        extractionSettings.regex = utils.getUniversalToDoRegex() if cmdLineSettings.bUniversalRegex else utils.getSinglelineRegexBy(extention)

    def extractLastExtention():
        return Path(cmdLineSettings.srcPath).suffixes.pop()[1:] #remove dot at the begining TODO: bug?

    extention = extractLastExtention()
    processNullExtention(extention)

    extractionSettings = ExtractionSettings()
    prepareExtractionSettings(extractionSettings)

    _extract(cmdLineSettings.srcPath, cmdLineSettings.outputPath, extractionSettings)

#TODO: arguments API has changed
def extractFromDirectory(cmdLineSettings: CmdLineSettings):

    def proccesOutputExistance():
        if cmdLineSettings.bOverwriteOutput is not True and os.path.exists(cmdLineSettings.outputPath):
            _terminateOnDstFileExistance(cmdLineSettings.outputPath)

    def prepareExtractionSettings(extractionSettings):
        extractionSettings.bOverwriteOutput = cmdLineSettings.bOverwriteOutput
        extractionSettings.bSameDirForOutput = False #because we need to solve dstPath here before the loop #TODO: I'm confused how _extract will process
        extractionSettings.bFromLoop = True
        extractionSettings.outputFileSettings.name = cmdLineSettings.outputName

    def resolveOutputPath():
        outputFilePathResolver = utils.OutputFilePathResolver(cmdLineSettings)
        cmdLineSettings.outputPath = outputFilePathResolver.resolvePath()

    def processFiles():
        for filePath, extention in utils.getFilteredListOfFiles(cmdLineSettings.srcPath, cmdLineSettings.extentionFilter):
            #TODO: refactor
            convention = UniversalConvention() if cmdLineSettings.bUniversalRegex else LeontkConvention()
            extractionSettings.regex = utils.getSinglelineRegexBy(extention, convention)
            _extract(filePath, cmdLineSettings.outputPath, extractionSettings)

    proccesOutputExistance()

    extractionSettings = ExtractionSettings()
    prepareExtractionSettings(extractionSettings)

    resolveOutputPath()
    processFiles()


class ExtractionContext:
    def __init__(self, cmdLineSettings) -> None:
        self.cmdLineSettings = cmdLineSettings
        
    def extract():
        pass


