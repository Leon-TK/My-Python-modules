#SPDX-FileCopyrightText: � 2022 Leonid Tkachenko leon24rus@gmail.com
#SPDX-License-Identifier: MIT License

import subprocess

from .shellInterface import Shell

class Powershell(Shell):
    def __init__(self) -> None:
        self.instance = None

    #TODO: name of exe can be different.
    def Init(self):
        self.instance =  subprocess.Popen(["powershell"], stdin=subprocess.PIPE, stdout = subprocess.PIPE,
                                        stderr = subprocess.PIPE, universal_newlines = True, bufsize = 0, shell = False)
    def Shutdown(self):
        self.instance.terminate()
    def SendMsg(self, msg):
        self.instance.stdin.write(msg)
    def ChangeDir(self, dir):
        self.instance.stdin.write(f"cd {dir}")
    def Execute(self, file, args, dir):
        self.instance.stdin.write(f"{dir}\\{file} {args}")
    def Readline(self) -> str:
        return self.instance.stdout.readline()
    def Readlines(self) -> str:
        return self.instance.stdout.readlines()
    
class Batch(Shell):
    pass
class Bash(Shell):
    pass