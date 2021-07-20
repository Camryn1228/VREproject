"""Imported the os class
'path_main variable stores the file folder I created
'files_and_directories is the list
 For loop iterates through the variables
 For loop also opens the file folder on
The 'Executables' folder is then extracted and read using the variables that are stored in the main file"""
import os
path_main =("C:/Users/noeli/PycharmProjects/Executables folder")#File folder I created to test code.
files_and_directories = os.listdir(path_main)

for file in files_and_directories:
    filepath = path_main+ "/" + file
os.startfile("C:/Users/noeli/PycharmProjects/Executables folder")
