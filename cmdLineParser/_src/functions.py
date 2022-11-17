from .parsers import StandardParser

def parseCmdLine(args: list) -> list:
    parser = StandardParser(args)
    return parser.parseArgs()

