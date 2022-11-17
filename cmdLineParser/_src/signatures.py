class KeyValueSignature:
    valueDelimiter = ''
    prefix = ''
class OptionSignature:
    prefix = ''

class StandardKeyValueSignature(KeyValueSignature):
    KeyValueSignature.valueDelimiter = '=' #TODO: will this change static class or this?
    KeyValueSignature.prefix = '-'
    assert(KeyValueSignature.prefix != KeyValueSignature.valueDelimiter)
class StandardOptionSignature(OptionSignature):
    OptionSignature.prefix = '-'