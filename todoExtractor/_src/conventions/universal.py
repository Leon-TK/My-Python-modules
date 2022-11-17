from .convention import SinglelineTodoConvention

class UniversalConvention(SinglelineTodoConvention):
    def __init__(self) -> None:
        super().__init__()
        self.regex = r"(?i:todo)[: ][^\r\n]+[\r\n]"
        self.description = "Universal convention"
        self.notes = "\'todo\' insensitive case, then comes whitespaces and further text until newline"