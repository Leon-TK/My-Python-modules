#SPDX-FileCopyrightText: � 2022 Leonid Tkachenko leon24rus@gmail.com
#SPDX-License-Identifier: MIT License

from .shellInterface import Shell
from .shellImplementation import Powershell

class SshWithShell():
    def __init__(self) -> None:
        self.shell = Powershell()
    def Init(self):
        self.shell.Init()
        print(self.shell.Readline())
    def Connect(self, host):
        self.SendMsg(f"ssh {host}")
        print(self.shell.Readline())
    def SendMsg(self, msg):
        self.shell.SendMsg(msg)
        print(self.shell.Readline())
    def ChangeDir(self, dir):
        self.shell.ChangeDir(dir)
        print(self.shell.Readline())
    def Exec(self, file, args, dir):
        self.shell.Execute(file, args, dir)
        print(self.shell.Readline())
    def Shutdown(self):
        self.SendMsg(f"exit")
        self.shell.Shutdown()