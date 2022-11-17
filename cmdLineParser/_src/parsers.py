from .arguments import KeyValue, Option, StandartKeyValueSignature,\
StandartOptionSignature, KeyValueSignature, OptionSignature
from . import constants

#TODO: use regex?

__all__ = ["StandardParser"]

class StandardParser:
    def __init__(self, args: list) -> None:
        self.args = args
        self.parsedArgs = []
        
    def parseArgs(self):
        for arg in self.args:
            parsed: KeyValue = self.__parseString(arg)
            self.parsedArgs.append(parsed)
        return self.parsedArgs
        
    def __parseString(self, arg: str) -> KeyValue:
        kvSignature: KeyValueSignature = StandartKeyValueSignature
        oSignature: OptionSignature = StandartOptionSignature

        isKV_l = lambda :\
            arg.find(kvSignature.prefix) == 0 and arg.find(kvSignature.valueDelimiter) > 0 #TODO: what if prefix + delimiter, eg -=?
        isOption_l = lambda : not isKV_l() and arg.find(oSignature.prefix) == 0
        
        def __processKv():
            kvObj = KeyValue()
            splitted = arg.split(kvSignature.valueDelimiter)
            assert (len(splitted) <= 2)
            prefixAndName = splitted[0].split(kvSignature.prefix) # [' ', name]
            assert(len(prefixAndName) == 2)
            if prefixAndName[0] == '':
                kvObj.key = prefixAndName[1]
            else:
                print(constants.BAD_KEY_ERROR + splitted[0])
                raise Exception
            kvObj.value = splitted[1]
            return kvObj

        def __processOption():
            optionObj = Option()

            splitted = arg.split(oSignature.prefix)
            assert(len(splitted) == 2)

            if splitted[0] == '':
                optionObj.value = splitted[1]
            else:
                print(constants.BAD_OPTION_ERROR + arg)
                raise Exception
            return optionObj

        if isKV_l():
            return __processKv()
        if isOption_l():
            return __processOption()
