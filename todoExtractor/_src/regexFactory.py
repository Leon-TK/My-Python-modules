from .conventions import convention

class RegexSinglelineTodoFactory:
    def __init__(self) -> None:
        pass
    def get(self) -> str:
        pass
class RegexMultilineTodoFactory:
    def __init__(self) -> None:
        pass
    def get(self) -> str:
        pass


class PythonRegexFactory(RegexSinglelineTodoFactory):
    def __init__(self, convention: convention.SinglelineTodoConvention) -> None:
        super().__init__()
        self._convention = convention
    def get(self) -> str:
        return r"# *" + self._convention.regex

class CRegexFactory(RegexSinglelineTodoFactory):
    def __init__(self, convention: convention.SinglelineTodoConvention) -> None:
        super().__init__()
        self._convention = convention
    def get(self) -> str:
        return r"// *" + self._convention.regex

class HtmlRegexFactory(RegexSinglelineTodoFactory):
    def __init__(self, convention: convention.SinglelineTodoConvention) -> None:
        super().__init__()
        self._convention = convention
    def get(self) -> str:
        return r"<!-- *" + self._convention.regex[:-1] + r"--> *[\r\n]"

class CssRegexFactory(RegexSinglelineTodoFactory):
    def __init__(self, convention: convention.SinglelineTodoConvention) -> None:
        super().__init__()
        self._convention = convention
    def get(self) -> str:
        return r"/\* *" + self._convention.regex[:-1] + r"\*/ *[\r\n]"

class PlainRegexFactory(RegexSinglelineTodoFactory):
    def __init__(self, convention: convention.SinglelineTodoConvention) -> None:
        super().__init__()
        self._convention = convention
    def get(self) -> str:
        return self._convention.regex