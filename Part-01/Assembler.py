### Program Name: Design An Assembler Part1.
### Author: Seyed Ali Maher
### Student NO.: 9932113
### Creation Date: 1400-09-03
### Revision: 00
### Program Description: Design an assembler that convert the assembly code to machine code. 
### In this part of project we assume that MOD = 11, which means data transferring is between
### registers only.



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  Read AsmCode Inputs File
asmCode = open("InputsAsmCodes.txt", "r")

asmCode = (asmCode.read()).replace(",","").splitlines()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  Define Functions
def select_Instruction(asmCode, roundd):
    
    if (asmCode[0].upper() == "ADD"):
        retCode = ADD_Instruct(asmCode[1].upper(), asmCode[2].upper())
        
    elif (asmCode[0].upper() == "SUB"):
        retCode = SUB_Instruct(asmCode[1].upper(), asmCode[2].upper())
    
    elif (asmCode[0].upper() == "AND"):
        retCode = AND_Instruct(asmCode[1].upper(), asmCode[2].upper())
    
    elif (asmCode[0].upper() == "OR"):
        retCode = OR_Instruct(asmCode[1].upper(), asmCode[2].upper())
    
    else:
        print("We Don't Have Such This Instruction.")
        return 0
    
    return retCode
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  Define Instructions
def ADD_Instruct(opd1, opd2):
 
    if opd1 in reg_8 and opd2 in reg_8:
        opd1 = reg_8.index(opd1)
        opd2 = reg_8.index(opd2)
        machineCode = '"\\' + (" x00") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
    
    elif opd1 in reg_16 and opd2 in reg_16:     
        opd1 = reg_16.index(opd1)
        opd2 = reg_16.index(opd2)
        machineCode = '"\\' + (" x66\ 0x01") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
    elif opd1 in reg_32 and opd2 in reg_32:     
        opd1 = reg_32.index(opd1)
        opd2 = reg_32.index(opd2)
        machineCode = '"\\' + (" x01") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
    elif opd2.isnumeric():                                                                                              # we don't support imm
        print("We Don't Support IMMs. Ishallah Part 2om Project.")
        machineCode = 0
        
    else:                                                                                                               # Operands Size Checking
        print("The Operands Must Have Same Size!")
        machineCode = 0

    return machineCode
    
    
def SUB_Instruct(opd1, opd2):
 
    if opd1 in reg_8 and opd2 in reg_8:
        opd1 = reg_8.index(opd1)
        opd2 = reg_8.index(opd2)
        machineCode = '"\\' + (" x28") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
    
    elif opd1 in reg_16 and opd2 in reg_16:     
        opd1 = reg_16.index(opd1)
        opd2 = reg_16.index(opd2)
        machineCode = '"\\' + (" x66\ 0x29") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
    elif opd1 in reg_32 and opd2 in reg_32:     
        opd1 = reg_32.index(opd1)
        opd2 = reg_32.index(opd2)
        machineCode = '"\\' + (" x29") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
    elif opd2.isnumeric():                                                                                              # we don't support imm
        print("We Don't Support IMMs. Ishallah Part 2om Project.")
        machineCode = 0
    
    else:                                                                                                               # Operands Size Checking
        print("The Operands Must Have Same Size!")
        machineCode = 0

    return machineCode
    

def AND_Instruct(opd1, opd2):
 
    if opd1 in reg_8 and opd2 in reg_8:
        opd1 = reg_8.index(opd1)
        opd2 = reg_8.index(opd2)
        machineCode = '"\\' + (" x20") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
    
    elif opd1 in reg_16 and opd2 in reg_16:     
        opd1 = reg_16.index(opd1)
        opd2 = reg_16.index(opd2)
        machineCode = '"\\' + (" x66\ 0x21") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
    elif opd1 in reg_32 and opd2 in reg_32:     
        opd1 = reg_32.index(opd1)
        opd2 = reg_32.index(opd2)
        machineCode = '"\\' + (" x21") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
    elif opd2.isnumeric():                                                                                              # we don't support imm
        print("We Don't Support IMMs. Ishallah Part 2om Project.")
        machineCode = 0
   
    else:                                                                                                               # Operands Size Checking
        print("The Operands Must Have Same Size!")
        machineCode = 0

    return machineCode
    
    
def OR_Instruct(opd1, opd2):
 
    if opd1 in reg_8 and opd2 in reg_8:
        opd1 = reg_8.index(opd1)
        opd2 = reg_8.index(opd2)
        machineCode = '"\\' + (" x08") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
    
    elif opd1 in reg_16 and opd2 in reg_16:     
        opd1 = reg_16.index(opd1)
        opd2 = reg_16.index(opd2)
        machineCode = '"\\' + (" x66\ 0x09") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
    elif opd1 in reg_32 and opd2 in reg_32:     
        opd1 = reg_32.index(opd1)
        opd2 = reg_32.index(opd2)
        machineCode = '"\\' + (" x09") + "\\ " + hex(int("11" + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
    
    elif opd2.isnumeric():                                                                                              # we don't support imm
        print("We Don't Support IMMs. Ishallah Part 2om Project.")
        machineCode = 0
        
    else:                                                                                                               # Operands Size Checking
        print("The Operands Must Have Same Size!")
        machineCode = 0

    return machineCode
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
        
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  Define Registers
reg_Value = ["000", "001", "010", "011", "100", "101", "110", "111"]
reg_8 = ["AL", "CL", "DL", "BL", "AH", "CH", "DH", "BH"]
reg_16 = ["AX", "CX", "DX", "BX", "SP", "BP", "SI", "DI"]
reg_32 = ["EAX", "ECX", "EDX", "EBX", "ESP", "EBP", "ESI", "EDI"]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  Printing Part   
for roundd in range(0, len(asmCode)):
    machineCode = select_Instruction(asmCode[roundd].split(), roundd)
    if (machineCode):
        print(machineCode)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
