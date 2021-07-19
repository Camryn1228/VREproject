import ExtactingData
import ImportsandExports

if __name__=='__groupcombo__':

    exe_path = input("Enter the path of your executable: ")  # path to executable ++.

    ExtactingData.extract(exe_path)
    ImportsandExports.run(exe_path)