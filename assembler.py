from enum import Enum


class Label(object):
    def __init__(self):
        self.indices = []  # Instructions will be stored in a list. This is the indicies of that list that need this label
        self.location = -1  # The location that the label references


class Operation(object):

    def __init__(self, opType, opCode, funCode=-1):
        self.opType = opType
        self.opCode = opCode
        self.funCode = funCode


def opDictFromFile(fName):
    inFile = open(fName, 'r')
    opDict = {}
    for line in inFile:
        lineList=line.split()

        if len(lineList)>0:
            lineList[1] = lineList[1]  # operation type (j,i,r)
            lineList[2] = int(lineList[2], 2)  # opcode

            if len(lineList) > 3:
                lineList[3] = int(lineList[3], 2)  # funcode
            else:
                lineList.append("")
                lineList[3] = -1

            opDict[lineList[0]] = Operation(lineList[1], lineList[2], lineList[3])

    return opDict


