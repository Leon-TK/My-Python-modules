import sys
from string import Template

from .interface import *

#TODO: Create normal implementation of cmd args processing
#TODO: add ability to exclude file/directory list
#TODO: add ability to choose regex (???)
#TODO: add ability to search in files without extention
#TODO: -excl option. should I add suboptions for this, for example if full path is specified, no need to find same files
#TODO: should I create module that extracts regex match strings into file?
#TODO: Add ANSI, ASCII encodings support
#TODO: sometimes a todo is extracted with precedent part of line, particulary "// TODO -"
#TODO: add thread pool for handling multiple files

def findIndexOf(obj: str, container) -> int|None:
    index = 0
    for elem in container:
        if obj in elem:
            return index
        index += 1
    return None

def parseListOption(option, kvDelimiter, valueDelimiter) -> list:
    return option.split(kvDelimiter)[1].split(valueDelimiter)

def getHelpMsg() -> str:
    template = """
        1. $d <dirpath> or $f <filepath>
        2. output file path, can ommit if $dOut is specified
        Any pos: $dOut save output file where input is,
        $o overwrite outputfile
        $t use timestemps
        $ext list file extentions. Must specify if $d. "," delimiter, whithout whitespaces
        $excl list files and dirs to exclude. NOT WORKING
        $u use universal regex for finding todo. This will find all common todos whitout any signature. (?i:todo)[: ][^\\r\\n]+[\\r\\n]
        $n <logname>
    """
    return Template(template).substitute(d=optionsMap["directoryFlag"], f=optionsMap["fileFlag"], dOut=optionsMap["cdwForOutput"],
    t=optionsMap["timestampInLog"], ext=optionsMap["extentionFilter"], excl=optionsMap["excludeFilter"], u=optionsMap["universalRegex"],
    n=optionsMap["outputName"], o=optionsMap["overwriteOutput"])

def resolveHelp(args):
    for hOption in optionsMap["help"]:
        if hOption in args:
            print(getHelpMsg())
            sys.exit(0)

def resolveExtentionFilter(args, settings: CmdLineSettings):
    extIndex = findIndexOf(optionsMap["extentionFilter"], args)
    if extIndex is not None:
        settings.extentionFilter = parseListOption(args[extIndex], "=", ",")

def prepareSettingsFrom(args):
    settings = CmdLineSettings()
    
    settings.srcPath = args[2]
    settings.bSameDirForOutput = optionsMap["cdwForOutput"] in args
    settings.outputPath = args[3] if not settings.bSameDirForOutput else ''
    
    settings.bUseTimestamp = optionsMap["timestampInLog"] in args
    settings.bUniversalRegex = optionsMap["universalRegex"] in args
    settings.bOverwriteOutput = optionsMap["overwriteOutput"] in args

    if optionsMap["outputName"] in sys.argv:
        settings.outputName = sys.argv[findIndexOf(optionsMap["outputName"], sys.argv) + 1]

    return settings

optionsMap = {"help": ["-help", "--help", "-h", "--h"], "directoryFlag": "-d", "fileFlag": "-f",
"overwriteOutput": "-o", "cdwForOutput": "-s", "timestampInLog": "-t", "extentionFilter": "-ext=", "excludeFilter": "-excl=",
"universalRegex": "-u", "outputName": "-n"}

def handleDIrectoryFlag(settings):
    resolveExtentionFilter(sys.argv, settings)
    #TODO: move bSameDirOutput condition implementation out of this function and pass processed directory path
    #TODO: move bUniversalRegex condition implementation out of this function and pass regex instead
    extractFromDirectory(settings)

def handleFileFlag(settings):
    #TODO: move bSameDirOutput condition implementation out of this function and pass processed directory path
    #TODO: move bUniversalRegex condition implementation out of this function and pass regex instead
    extractFromFile(settings)

if __name__ == "__main__":

    resolveHelp(sys.argv)

    firstArg = sys.argv[1]

    settings = prepareSettingsFrom(sys.argv)

    if firstArg == optionsMap["directoryFlag"]:
        handleDIrectoryFlag(settings)

    elif firstArg == optionsMap["fileFlag"]:
        handleFileFlag(settings)