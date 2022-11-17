#SPDX-FileCopyrightText: 2022 Leonid Tkachenko leontkdev@gmail.com
#SPDX-License-Identifier: MIT License

from .interface import *
import sys #TODO: how to hide this when importing this package?

#TODO: can be multiple SPDX lines?
#TODO: Make interface for command line use

if __name__ == "__main__":
    if "-help" in sys.argv:
        print("""
        Cmd line mode doesn't work for now, use -interactive
        1. holder name. Or -interactive for entering interactive mode
        2. email
        3. licence
        4. path
        5. action
        """)
    try:
        bInteracriveMode = sys.argv[1] == "-interactive"
    except IndexError:
        print("Error. Missing 1 argument - holder or -interactive")
        sys.exit(0)

    if bInteracriveMode:
        beginInteractiveMode()
    else:
        beginCmdLineMode()

    