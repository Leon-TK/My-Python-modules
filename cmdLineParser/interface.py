""" args - command line arguments. implementation expects sys.args
    sys.args contains space separated values. This parser works with KV signatures with no spaces, that is args contains kv pairs """
from ._src.functions import parseCmdLine

from ._src.parsers import StandardParser