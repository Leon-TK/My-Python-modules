#I'm using non static vars, because child classes will raise if have not defined variables
class SinglelineTodoConvention:
    def __init__(self) -> None:
        self.regex: str = ""
        self.description: str = ""
        self.notes: str = ""