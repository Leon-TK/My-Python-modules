import fileExtentionsConstants as fileExtentions

from . import constants

#TODO: add description for variables

class OutputFileSettings():
    def __init__(self) -> None:
        self.bUseTimestamp = True
        self.bUseTimestampInFileName = False
        self.name = constants.DEFAULT_OUTPUT_NAME #TODO: should change this depent of bUseTimestampInFileName or SRP will be failed? #TODO: for now it's redundant because of OutputFilePathResolver class using cmdLineSettings instead

class ExtractionSettings():
    def __init__(self) -> None:
        #What to extract from a file
        self.regex = ''
        self.bOverwriteOutput = False
        self.bSameDirForOutput = True
        #Util variable
        self.bFromLoop = False
        self.outputFileSettings = OutputFileSettings()

#Parsed cmd line
class CmdLineSettings():
    def __init__(self) -> None:
        self.bOverwriteOutput = False
        self.bSameDirForOutput = True
        self.bUniversalRegex = False
        self.extentionFilter = fileExtentions.PLAINTEXT_EXTS
        self.srcPath = r''
        self.outputPath = r'' #TODO: full path or dir path?, for now it's dir!
        self.outputName = None
        self.bUseTimestamp = True
