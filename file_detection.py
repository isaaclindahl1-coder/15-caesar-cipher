import os

"""
file detection needs checking if a file or folder exists in agiven location
before your program tries to do anything with it

in python, to work you need the os module. the os module is for interacting with the operating system
"""

file_path = "test.txt" #note this is a relative path
#relative means, based on from the present working dictionary (where the program is running)


#see if our file exists
if os.path.exists(file_path):
    print(f"the file path {file_path} exists.")
else:
    print(f"the file path {file_path} does not exists.")

file_path2 = "text_files/test2,txt"


if os.path.exists(file_path2): #relative path
    print(f"the file path {file_path2} exists.")
else:
    print(f"the file path {file_path2} does not exists.")




#bad - SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
file_path3 = "C:\Users\CMP_jalarkin\16 file handing\text_files\test2.txt"
#works - forward slash
file_path3 = "C:/Users/CMP_jalarkin/16 file handing/text_files/test2.txt"
#works - double backslash
file_path3 = "C:\\Users\\CMP_jalarkin\\16 file handing\\text_files\\test2.txt"
#works - raw strings place r before the string


#detecting if its a file or a folder:
if os.path.exists(file_path2): 
    if os.path.isfile(file_path3):
        print(f"the file path {file_path2} exists if file.")
    elif os.path.isdir(file_path3):
            print(f"the file path {file_path2} exists if directory.")
else:
        print(f"the file path {file_path} does not exists.")

#decting if a path is valid 
# determing if it is a file or directory
#relative vs absolute paths