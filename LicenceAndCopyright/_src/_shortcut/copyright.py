from enum import Enum
from abc import ABC, abstractmethod

class ECopyrightShortcut(Enum):
    SPDX = 0

class CopyrightShortcut(ABC):
    @abstractmethod
    def getStr(self) -> str:
        pass

class SpdxCopyrightShortcut(CopyrightShortcut):
    def __init__(self, year, holder, email):
        self.data = f"SPDX-FileCopyrightText: © {year} {holder} {email}"

    def getStr(self) -> str:
        return self.data