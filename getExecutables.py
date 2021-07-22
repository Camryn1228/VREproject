"""Imported the os class
'exe_path' variable stores user input
'files_and_directories' lists 'exe_path'
 For loop iterates through the variables"""
import os


def get_executables():
    exe_path = input("Enter the path of your executable: ")  # path to executable ++.
    files_and_directories = os.listdir(exe_path)

    for file in files_and_directories:
        filepath = exe_path+ "/" + file
        ExtactingData.extract(exe_path)
        ImportsandExports.run(exe_path)



get_executables()