#Simple Python program to rename files in a directory to conform with plex standard: 'Example - S01E01'.
#You will be prompted to enter file format, file name, season, and starting episode.

import os
from os import listdir

directory = input("Enter full directory path:")

# adds a trailing / to the user input file directory if it's not already there.
if directory.endswith("/"):
    pass
else:
    directory = directory + "/"

# checks if valid directory.
valid_directory = os.path.isdir(directory)


if valid_directory:
    files_dir = listdir(directory)

    # this step is necessary to sort the files in the list.
    files_dir.sort()

    # creating variables from user input.
    a = []
    file_format = input("Enter file format. Example '.mkv','.mp4','.avi' : ")
    file_name = input("Enter TV_show name name. Example 'One Piece' : ")
    season = input("Enter Season Number. Example '01','02','03','04' : ")
    starting_episode = int(input("Enter Starting Episode Number. Example '1','2','3','4' : "))

    # checks for file format in the files.
    for item in files_dir:
        if file_format in item:
            x = (directory + item)
            a.append(x)
        else:
            print("Could not find file format in directory.")
    
    # for every file in the list, rename it as 'Example - S01E01'.
    for item in a:
        os.rename(item,directory + file_name + ' - S' + season.zfill(2) + "E" + str(starting_episode).zfill(2) + file_format)
        starting_episode = starting_episode + 1
else:
    print("Invalid directory path.")