### Program Description: Check The right name in Assembly
### Author: Seyed Ali Maher
### Student NO.: 9932113
### Creation Date: 2021-10-04

INPUT = input("Enter Your var as input: ")
VAR = INPUT

truth_state = 1
err_flag = 0

Max_Len = 248

INPUT = INPUT + "\n" ## a trick. when we read a file with .readlines()
                    ### we have the elements with '\n' at the end like
                    ### mov\n , ADD\n , ... . so inorder to check if it
                    ### is in the file or not we should add '\n'.

################################# Reading Resereved Words File

File_RW = open("Rwords_in_asm.txt")

if(INPUT in File_RW. readlines()):
    
    print(VAR, " can't be an identifier!")
    err_flag = 1
    
################################
    
INPUT = INPUT.replace(INPUT[-1],'') ## end of the trick. we should remove
                                    ## '\n' from the Inputs.
    
INPUT = INPUT.upper() ### Assembly isn't Case Sensitive. so with .upper()
                       ## we consider that (ADD == add) = true.
    
if(err_flag == 0):
    
    if (len(INPUT) < Max_Len) and (len(INPUT)):
        
        if (INPUT[0] in ['@', '$', '_', '?'] or INPUT[0].isalpha()):
            
            for IDX_ChChar in range (1,len(INPUT)):  ### we use this loop to show The character(Except the first)
                                                           ## or characters which is used in input is valid or not.
                if (INPUT[IDX_ChChar] not in ['@', '$', '_', '?'] and not(INPUT[IDX_ChChar].isalpha()) and not(INPUT[IDX_ChChar].isdigit())):
                    truth_state = 0
                    
            if truth_state:
                print(VAR, " can be an identifier!")
            else:
                print(VAR, " can't be an identifier!")
                err_flag = 4
                
        else:
            print(VAR, " can't be an identifier!")
            err_flag = 3
            
    else:
        print(VAR, " can't be an identifier!")
        err_flag = 2

#################### Error Finding Part
# this part help us to find where the problem occured.

if err_flag == 0:
    print("No Error :)")
elif err_flag == 1:
    print("Error: This is a reserved word!")
elif err_flag == 2:
    print("Error: Lenght of the input isn't in correct range!")
elif err_flag == 3:
    print("Error: The first character is wrong!")
else:#err_flag == 4
    print("Error: Invalid character(Except the first char) is used!")
    
#################### End Of Error finding part
    
File_RW.close()