FIRST_INSTRUCTION_ADDRESS = 0

class Label(object):
    def __init__(self):
        self.indices = []  # Instructions will be stored in a list. This is the indices of that list that need this label
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


def regNumfromNotation(regNotation):
    regNotation=regNotation.replace(",","")
    regNotation=regNotation.replace("$","")
    return int(regNotation)


def rType(line,opDict):
    lineList=line.split()
    opCode=opDict[lineList[0]].opCode
    funCode=opDict[lineList[0]].funCode
    shamt=0

    if lineList[0] == "jr":
        rd=0
        rs=regNumfromNotation(lineList[1])
        rt=0
    elif lineList[0] == "sll" or lineList[0] == "srl":
        rd=regNumfromNotation(lineList[1])
        rs=0
        rt=regNumfromNotation(lineList[2])
        shamt=int(lineList[3],16)
    else:
        rd=regNumfromNotation(lineList[1])
        rs=regNumfromNotation(lineList[2])
        rt=regNumfromNotation(lineList[3])

    opCode=bin(opCode)[2:].zfill(6)
    funCode=bin(funCode)[2:].zfill(6)
    rd=bin(rd)[2:].zfill(5)
    rs=bin(rs)[2:].zfill(5)
    rt=bin(rt)[2:].zfill(5)
    shamt=bin(shamt)[2:].zfill(5)

    return opCode+rs+rt+rd+shamt+funCode


def iType(line,opDict):
    lineList=line.split()
    opCode=opDict[lineList[0]].opCode

    if lineList[0] == "beq":
        rt=regNumfromNotation(lineList[2])
        rs=regNumfromNotation(lineList[1])
        imm=int(lineList[3],16)
    else:
        rt=regNumfromNotation(lineList[1])
        rs=regNumfromNotation(lineList[2])
        imm=int(lineList[3],16)

    opCode=bin(opCode)[2:].zfill(6)
    rs=bin(rs)[2:].zfill(5)
    rt=bin(rt)[2:].zfill(5)
    imm=bin(imm & 0xffff)[2:].zfill(16)

    return opCode+rs+rt+imm


def jType(line, opDict, labels, arrayIdx):
    lineList=line.split()
    opCode=opDict[lineList[0]].opCode
    opCode=bin(opCode)[2:].zfill(6)

    if lineList[0] == "halt":
        return opCode + "1"*26
    else:
        if lineList[1] not in labels:
            labels[lineList[1]]=Label()
        labels[lineList[1]].indices.append(arrayIdx)  # I'll use this to find it later

        return opCode  # the address gets tacked on in resolveLabels


def resolveLabels(labels,instructions):
    for label in labels:
        for idx in labels[label].indices:
            addr=bin(labels[label].location)[2:].zfill(26)
            instructions[idx]=instructions[idx]+addr


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
            labels[line].location = currentAddress + 4
        elif line.split() == []:
            pass  # empty line
        else:
            operation=line.split()[0]
            if operation not in opDict:
                print("Unknown instruction '"+operation+"' from line '"+line[:-1]+"'")
                exit(1)

            currentAddress += 4

            if opDict[operation].opType == 'r':
                instructions.append(rType(line,opDict))
            elif opDict[operation].opType == 'i':
                instructions.append(iType(line,opDict))
            elif opDict[operation].opType == 'j':
                instructions.append(jType(line, opDict, labels, (len(instructions))))
            else:
                print("Unrecognized type:", opDict[operation].opType)
                exit(1)

    resolveLabels(labels, instructions)

    return instructions


dotSFile=input("Please enter the location of the file to assemble: ")
instr=assemble(dotSFile)
for inst in instr:
    print(inst)
