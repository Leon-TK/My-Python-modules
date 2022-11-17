#SPDX-FileCopyrightText: � 2022 Leonid Tkachenko leon24rus@gmail.com
#SPDX-License-Identifier: MIT License

import os
import re
import sys
toDo ya asdasd asdasd
#TODO: extraction funcs cannot find TODOs in multiline comments # TODO: test2 TODO: sdasd
#TODO: extractor saves whole comment line. do separate all todos in that line. remark - there can be situation like this "# todocontent TODO"
#TODO: can be situations when in output file could be duplicate todo's. ProcessDstFileExisting preventes this, but things tend to change
#TODO: delete file if there no TODOs

SRC_PATH = "E:\\Source\\Scripts\\todoExtractor\\test"
DST_PATH = "E:\\Source\\Scripts\\todoExtractor\\test\\test.txt"

PY_REGEX = r'#[^S\r\n]*TODO:[^S\r\n]*\s' # one line comment
MY_REGEX = r"(H|h)andle" #Find where I wrote this)

def GetTodoRegex(commentChar) -> str:
    return commentChar + r"[^S\r\n]*TODO:[^S\r\n]*\s"

def GetPythonTodoRegex() ->str:
    return GetTodoRegex('#')
def GetCTodoRegex() ->str:
    return GetTodoRegex('//')

def ProcessDstFileExistance(dstPath):
    #TODO: Throw exception?
    print(f"Output file already exists - {dstPath}\nUse another file name") # it's for safety
    sys.exit(0)

#Saves all matches into file
def extractFromFile(path, dstPath, regex, bIgnoreExistingFile = False):
    if os.path.exists(dstPath) and bIgnoreExistingFile is not True:
        ProcessDstFileExistance(dstPath)

    with open(path, 'r', encoding="utf-8") as src, open(dstPath, 'a', encoding="utf-8") as dst:
        buffer = None
        try:
            buffer = src.readlines()
        except UnicodeDecodeError:
            print(f"Unicode error in {path}")
            return
        lineCount = 0
        for line in buffer:
            #TODO: what if multiline case?
            result = re.search(regex, line)
            if result is not None:
                dst.write(f"File - {path}, line - {lineCount + 1}, {line[result.start():]}\n")
                #TODO: flush for safety?
            lineCount += 1

def extractFromDirectory(path, extentions, dstPath, regex):
    if os.path.exists(dstPath):
        ProcessDstFileExistance(dstPath)

    for rootDir, nestedDirs, filePath in __listfiles(path, extentions):
        extractFromFile(filePath, dstPath, regex, True)

# returns list of files with given extention
# generator
def __listfiles(directory, extentions):
    for rootDir, dirs, names in os.walk(directory):
        for name in names:
            ext = os.path.splitext(name)[-1].lstrip('.')
            if ext in extentions:
                yield rootDir, name, os.path.join(rootDir, name)

def extractFromPythonFile(filePath, dstPath):
    extractFromFile(filePath, dstPath, GetPythonTodoRegex())
def extractFromPythonDirectory(dirPath, dstPath):
    extentions = ['py']
    extractFromDirectory(dirPath, extentions, dstPath, GetPythonTodoRegex())

if __name__ == "__main__":
    extractFromPythonDirectory(SRC_PATH, DST_PATH)