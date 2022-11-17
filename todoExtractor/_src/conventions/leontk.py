from .convention import SinglelineTodoConvention

class LeontkConvention(SinglelineTodoConvention):
    def __init__(self) -> None:
        super().__init__()
        self.regex = r"TODO *: *[^\r\n]+[\r\n]"
        self.description = "LeonTK's todo convention v1.0"