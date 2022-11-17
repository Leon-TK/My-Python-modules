from . import extractor
from . import utils

def extractFromPythonFile(filePath, dstPath):
    extractor._extract(filePath, dstPath, utils.getPythonTodoRegex())
    
def extractFromPythonDirectory(dirPath, dstPath):
    extentions = ['py']
    extractor.extractFromDirectory(dirPath, extentions, dstPath)