"""
why write to files
- hold imformation such as game scrores, user setting, notes or logs, large datasets

3 common types of datafiles 
1. plain text (.txt)
2. comma seperatred values (.csv)
3. json (javascript object notation) (.json)

"""

#writting to plain text file:
text_data = "um....gibebrish"
file_path = "text_files/test2.txt" # this is where we will save our data
#the preferred way and safest way to handle files is with the WITH statement
#with will open the file and automatically close it (free the resoures) even is an error occurs.
#open is the function to open the file. "w" opens it in write modes
#note with "w" if the file already exists it will be over written


with open(file_path, "w") as file:
    file.write(text_data)


#../ means go up one directory
file_path2 = "../annoying file.txt"
with open(file_path2, "w") as file:
    file.write("I am a super annoying file. can find me")

import os

#use with caution
#delete a file 
if os.path.exists(file_path2):
    os.remove(file_path2)


#but what if we dont want to overwrite the file everytime
# instead of using "w " we use "a" which means append

    file.write("\nsomething about inflation")


#there is a x (exclusive creation)flag you can use which will thor an error if the file already exists:
#so if you want to create a file but not overwite ome

try:
    with open(file_path, "x") as file:
        file.write("im here cause no file")
    print("file created")
except FileExistsError:
    print("that file already exists")


colors = ["blue", "maroon", "purple", "red", "green"]



with open("colors.txt", "w") as file:
    for color in colors:
        file. write(color + "\n")

