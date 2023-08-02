### Program Name: Design An Assembler Part2.
### Author: Seyed Ali Maher
### Student NO.: 9932113
### Creation Date: 1400-09-22
### Revision: 00
### Program Description: Design an assembler that convert the assembly code to machine code. 
### Improvements: In this part we also support the registers indirect addressing mode or 
### in the other word, SIB with no displacement, so we assume MOD = 00. 
### Note that we support the last part (MOD = 11) as well.

### Warning 1: We don't support 16 bits in MOD = 00!
### Warning 2: Because we don't have displacements so we consider ah, ch, esp and ebp same as
### other registers (No SIB).



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  Sources
# http://www.c-jump.com/CIS77/CPU/x86/lecture.html#X77_0210_encoding_add_immediate

# http://shell-storm.org/online/Online-Assembler-and-Disassembler/

# And a great thanks to Mr. Mirhosseini for his awsome guidance.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  Read AsmCode Inputs File
asmCode = open("InputsAsmCodes.txt", "r")

asmCode = (asmCode.read()).replace(",","").splitlines()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  Define Registers
reg_Value = ["000", "001", "010", "011", "100", "101", "110", "111"]
reg_8 = ["AL", "CL", "DL", "BL", "AH", "CH", "DH", "BH"]
reg_16 = ["AX", "CX", "DX", "BX", "SP", "BP", "SI", "DI"]
reg_32 = ["EAX", "ECX", "EDX", "EBX", "ESP", "EBP", "ESI", "EDI"]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  Define Functions
# Specify Direction Bit
def select_Direction(asmCode, roundd):
    asmCode = (asmCode[roundd].split())
    if ('[' in asmCode[1]):
        DirectBit = "0"
        
    else:
        DirectBit = "1"
    
    return DirectBit


# Specify MOD Bits
def select_MOD(asmCode, roundd):
    if ("[" in asmCode[roundd] and "]" in asmCode[roundd]):
        MOD = "00"
        for i in range(0, len(asmCode)):                                                                                    # Deleting the '[' and ']'
            if ("[" in asmCode[roundd] or "]" in asmCode[roundd]):
                asmCode[roundd] = asmCode[roundd].replace("[","")
                asmCode[roundd] = asmCode[roundd].replace("]","")
    
    else:
        MOD = "11"
        
    return MOD
    

# Specify Instruction
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
# MOD = 11: Reg to Reg
    if (MOD == "11"):
 
        if opd1 in reg_8 and opd2 in reg_8:
            opd1 = reg_8.index(opd1)
            opd2 = reg_8.index(opd2)
            machineCode = '"\\' + (" x00") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
        elif opd1 in reg_16 and opd2 in reg_16:     
            opd1 = reg_16.index(opd1)
            opd2 = reg_16.index(opd2)
            machineCode = '"\\' + (" x66\ 0x01") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
            
        elif opd1 in reg_32 and opd2 in reg_32:     
            opd1 = reg_32.index(opd1)
            opd2 = reg_32.index(opd2)
            machineCode = '"\\' + (" x01") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
            
        elif opd2.isnumeric():                                                                                              # We don't support imm
            print("We Don't Support IMMs. Ishallah in future.")
            machineCode = 0
            
        else:                                                                                                               # Operands Size Checking
            print("The Operands Must Have Same Size!")
            machineCode = 0
            

# MOD = 00: Mem to Reg or Reg to Mem    
    else:                                                                                                                   
        
        if opd1 in reg_8 and opd2 in reg_8:
            opd1 = reg_8.index(opd1)
            opd2 = reg_8.index(opd2)
            machineCode = '"\\ ' + hex(int("000000" + DirectBit + "0", 2)) + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1] \
                                   if int(DirectBit) == 0 else MOD + reg_Value[opd1] + reg_Value[opd2], 2)) + '"'
                                  
        elif opd1 in reg_32 and opd2 in reg_32:     
            opd1 = reg_32.index(opd1)
            opd2 = reg_32.index(opd2)
            machineCode = '"\\ ' + hex(int("000000" + DirectBit + "1", 2)) + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1] \
                                   if int(DirectBit) == 0 else MOD + reg_Value[opd1] + reg_Value[opd2], 2)) + '"'
            
        elif opd2.isnumeric():                                                                                              # We don't support imm
            print("We Don't Support IMMs. Ishallah in future.")
            machineCode = 0
            
        else:                                                                                                               # Operands Size Checking
            print("The Operands Must Have Same Size!")
            machineCode = 0

    return machineCode
    
    
def SUB_Instruct(opd1, opd2):
# MOD = 11: Reg to Reg
    if (MOD == "11"):
 
        if opd1 in reg_8 and opd2 in reg_8:
            opd1 = reg_8.index(opd1)
            opd2 = reg_8.index(opd2)
            machineCode = '"\\' + (" x28") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
        elif opd1 in reg_16 and opd2 in reg_16:     
            opd1 = reg_16.index(opd1)
            opd2 = reg_16.index(opd2)
            machineCode = '"\\' + (" x66\ 0x29") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
            
        elif opd1 in reg_32 and opd2 in reg_32:     
            opd1 = reg_32.index(opd1)
            opd2 = reg_32.index(opd2)
            machineCode = '"\\' + (" x29") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
            
        elif opd2.isnumeric():                                                                                              # we don't support imm
            print("We Don't Support IMMs. Ishallah in future.")
            machineCode = 0
        
        else:                                                                                                               # Operands Size Checking
            print("The Operands Must Have Same Size!")
            machineCode = 0
            

# MOD = 00: Mem to Reg or Reg to Mem    
    else:                                                                                                                   
        
        if opd1 in reg_8 and opd2 in reg_8:
            opd1 = reg_8.index(opd1)
            opd2 = reg_8.index(opd2)
            machineCode = '"\\ ' + hex(int("001010" + DirectBit + "0", 2)) + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1] \
                                   if int(DirectBit) == 0 else MOD + reg_Value[opd1] + reg_Value[opd2], 2)) + '"'
                    
        elif opd1 in reg_32 and opd2 in reg_32:     
            opd1 = reg_32.index(opd1)
            opd2 = reg_32.index(opd2)
            machineCode = '"\\ ' + hex(int("001010" + DirectBit + "1", 2)) + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1] \
                                   if int(DirectBit) == 0 else MOD + reg_Value[opd1] + reg_Value[opd2], 2)) + '"'
            
        elif opd2.isnumeric():                                                                                              # We don't support imm
            print("We Don't Support IMMs. Ishallah in future.")
            machineCode = 0
            
        else:                                                                                                               # Operands Size Checking
            print("The Operands Must Have Same Size!")
            machineCode = 0

    return machineCode
    

def AND_Instruct(opd1, opd2):
# MOD = 11: Reg to Reg
    if (MOD == "11"):
 
        if opd1 in reg_8 and opd2 in reg_8:
            opd1 = reg_8.index(opd1)
            opd2 = reg_8.index(opd2)
            machineCode = '"\\' + (" x20") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
        elif opd1 in reg_16 and opd2 in reg_16:     
            opd1 = reg_16.index(opd1)
            opd2 = reg_16.index(opd2)
            machineCode = '"\\' + (" x66\ 0x21") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
            
        elif opd1 in reg_32 and opd2 in reg_32:     
            opd1 = reg_32.index(opd1)
            opd2 = reg_32.index(opd2)
            machineCode = '"\\' + (" x21") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
            
        elif opd2.isnumeric():                                                                                              # we don't support imm
            print("We Don't Support IMMs. Ishallah in future.")
            machineCode = 0
       
        else:                                                                                                               # Operands Size Checking
            print("The Operands Must Have Same Size!")
            machineCode = 0
          
            
# MOD = 00: Mem to Reg or Reg to Mem    
    else:                                                                                                                   
        
        if opd1 in reg_8 and opd2 in reg_8:
            opd1 = reg_8.index(opd1)
            opd2 = reg_8.index(opd2)
            machineCode = '"\\ ' + hex(int("001000" + DirectBit + "0", 2)) + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1] \
                                   if int(DirectBit) == 0 else MOD + reg_Value[opd1] + reg_Value[opd2], 2)) + '"'
                    
        elif opd1 in reg_32 and opd2 in reg_32:     
            opd1 = reg_32.index(opd1)
            opd2 = reg_32.index(opd2)
            machineCode = '"\\ ' + hex(int("001000" + DirectBit + "1", 2)) + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1] \
                                   if int(DirectBit) == 0 else MOD + reg_Value[opd1] + reg_Value[opd2], 2)) + '"'
            
        elif opd2.isnumeric():                                                                                              # We don't support imm
            print("We Don't Support IMMs. Ishallah in future.")
            machineCode = 0
            
        else:                                                                                                               # Operands Size Checking
            print("The Operands Must Have Same Size!")
            machineCode = 0    

    return machineCode
    
    
def OR_Instruct(opd1, opd2):
# MOD = 11: Reg to Reg
    if (MOD == "11"):
    
        if opd1 in reg_8 and opd2 in reg_8:
            opd1 = reg_8.index(opd1)
            opd2 = reg_8.index(opd2)
            machineCode = '"\\' + (" x08") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
        elif opd1 in reg_16 and opd2 in reg_16:     
            opd1 = reg_16.index(opd1)
            opd2 = reg_16.index(opd2)
            machineCode = '"\\' + (" x66\ 0x09") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
            
        elif opd1 in reg_32 and opd2 in reg_32:     
            opd1 = reg_32.index(opd1)
            opd2 = reg_32.index(opd2)
            machineCode = '"\\' + (" x09") + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1], 2)) + '"'
        
        elif opd2.isnumeric():                                                                                              # we don't support imm
            print("We Don't Support IMMs. Ishallah in future.")
            machineCode = 0
            
        else:                                                                                                               # Operands Size Checking
            print("The Operands Must Have Same Size!")
            machineCode = 0
            
            
# MOD = 00: Mem to Reg or Reg to Mem    
    else:                                                                                                                   
        
        if opd1 in reg_8 and opd2 in reg_8:
            opd1 = reg_8.index(opd1)
            opd2 = reg_8.index(opd2)
            machineCode = '"\\ ' + hex(int("000010" + DirectBit + "0", 2)) + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1] \
                                   if int(DirectBit) == 0 else MOD + reg_Value[opd1] + reg_Value[opd2], 2)) + '"'
                    
        elif opd1 in reg_32 and opd2 in reg_32:     
            opd1 = reg_32.index(opd1)
            opd2 = reg_32.index(opd2)
            machineCode = '"\\ ' + hex(int("000010" + DirectBit + "1", 2)) + "\\ " + hex(int(MOD + reg_Value[opd2] + reg_Value[opd1] \
                                   if int(DirectBit) == 0 else MOD + reg_Value[opd1] + reg_Value[opd2], 2)) + '"'
            
        elif opd2.isnumeric():                                                                                              # We don't support imm
            print("We Don't Support IMMs. Ishallah in future.")
            machineCode = 0
            
        else:                                                                                                               # Operands Size Checking
            print("The Operands Must Have Same Size!")
            machineCode = 0    

    return machineCode
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  Printing Part   
for roundd in range(0, len(asmCode)):
    DirectBit = select_Direction(asmCode, roundd)
    MOD = select_MOD(asmCode, roundd)
    machineCode = select_Instruction(asmCode[roundd].split(), roundd)
    if (machineCode):
        print(machineCode)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #