#SPDX-FileCopyrightText: © 2022 Leonid Tkachenko leon24rus@gmail.com
#SPDX-License-Identifier: MIT License

import subprocess
from abc import ABC, abstractmethod

class Shell(ABC):
    @abstractmethod
    def Init(self):
        pass
    @abstractmethod
    def Shutdown(self):
        pass
    @abstractmethod
    def SendMsg(self, msg):
        pass
    @abstractmethod
    def ChangeDir(self, dir):
        pass
    @abstractmethod
    def Execute(self, file, args, dir):
        pass
    @abstractmethod
    def Readline(self) -> str:
        pass
    @abstractmethod
    def Readlines(self) -> str:
        pass