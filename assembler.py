FIRST_INSTRUCTION_ADDRESS=1

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

def rType(line,opDict):
    return -1

def iType(line,opDict):
    return -1

def jType(line, opDict, labels):
    return -1


def assemble(inFName):
    inFile= open(inFName, 'r')
    instructions=[]
    currentAddress=FIRST_INSTRUCTION_ADDRESS
    opDict=opDictFromFile("operations.txt")
    labels={}

    for line in inFile:
        if '#' in line[:2] :
            pass  # this is a comment
        elif line[0].isupper():
            line = line.replace(":","")
            line = line.replace(" ","")
            line = line.replace("\n","")
            if line not in labels:
                labels[line] = Label()
            labels[line].location = currentAddress  # TODO maybe plus 4
        elif line.split() == []:
            pass  # empty line
        else:
            operation=line.split()[0]
            if operation not in opDict:
                print("Unknown instruction '"+operation+"' from line '"+line[:-1]+"'")
                exit(1)

            currentAddress+=4

            if opDict[operation].opType == 'r':
                instructions.append(rType(operation,opDict))
            elif opDict[operation].opType == 'i':
                instructions.append(iType(operation,opDict))
            elif opDict[operation].opType == 'j':
                instructions.append(jType(operation,opDict, labels))
            else:
                print("Unrecognized type:" , opDict[operation].opType)

    return instructions

print(assemble("mult3.S"))
