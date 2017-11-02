from enum import Enum


class OpType(Enum):
    r = 1
    i = 2
    j = 3


class Operation(object):

    def __init__(self, opType, opCode, funCode = -1):
        self.opType = opType
        self.opCode = opCode
        self.funCode = funCode