import ExtactingData
import ImportsandExports
import getExecutables

if __name__=='__main__':

    exe_path = input("Enter the path of your executable: ")  # path to executable ++.

    ExtactingData.extract(exe_path)
    ImportsandExports.run(exe_path)
    getExecutables.get_executables()