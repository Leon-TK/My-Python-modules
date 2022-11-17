from abc import ABC, abstractmethod
from enum import Enum

class ELicenseShortcut(Enum):
    SPDX = 0

class LicenseShortcut(ABC):
    @abstractmethod
    def getStr(self) -> str:
        pass

class SpdxLicenseShortcut(LicenseShortcut):
    def __init__(self, license):
        self.data = f"SPDX-License-Identifier: {license}"

    def getStr(self) -> str:
        return self.data