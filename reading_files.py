"""
reading from files allows us to import and process wxisting data
"""
try:
    file_path = "colors.txt"
    with open(file_path, "r"):
        content = file.read() #read in entire file
    print(content)
except FileNotFoundError:
    print("do not exist")
except PermissionError:
    print("you no permission")


#readin the file one line at a time
colors = []
try:
    file_path = "colors.txt"
    with open(file_path, "r"):
        for line in file:
            colors.append(line.strip())
except FileNotFoundError:
    print("do not exist")
except PermissionError:
    print("you no permission")