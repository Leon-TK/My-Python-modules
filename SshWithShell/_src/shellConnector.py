#SPDX-FileCopyrightText: � 2022 Leonid Tkachenko leon24rus@gmail.com
#SPDX-License-Identifier: MIT License

from .shellInterface import Shell
from .shellImplementation import Powershell

class PowershellConnectror():
    def __init__(self) -> None:
        self.connector: Shell = Powershell()
    def Init(self):
        self.connector.Init()
    #returns responce
    def SendMsg(self, msg) -> str:
        self.connector.SendMsg(msg)
        return self.connector.ReadLine()
    def Shutdown(self, ):
        self.connector.Shutdown()