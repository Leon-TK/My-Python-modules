import sys
import re
from string import Template

"""Prints all assigned shortkeys without <unassigned> ones"""
"""Tested on 3ds max 2020"""
"""Place script into your PATH, run python -m PrintMaxHotkeys <hsx-file-path>\
    or create symbollink of python.exe with script path (or -m approach) and drag hsx file (win10)"""

#FUTURE: key value parse implementatios is trivial and not fully correct, if autodesk will change something, problems may appear. xml parser is prefered

TEMPLATE_REGEX = r"(?i:$key) *= *\"(?P<value>[^\r\n\"]*)\""

def processLine(line):
    if "Assign_Hotkey" in line:
        template = Template(TEMPLATE_REGEX)
        shortcut = re.search(template.safe_substitute(key="Shortcut"), line).group("value")
        description =  re.search(template.safe_substitute(key="Description"), line).group("value")
        print(f"\"{shortcut}\" - {description}")

def oneThread(fileBuffer):
    for line in fileBuffer:
            processLine(line)

def main():
    hotkeysFilePath = sys.argv[1]

    with open(hotkeysFilePath, "r") as hotkeysFIle:
        fileBuffer = hotkeysFIle.readlines()

        oneThread(fileBuffer)
    input()

if __name__ == "__main__":
    main()
        

