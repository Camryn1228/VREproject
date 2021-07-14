import pefile

def extract():
    exe_path = input("Enter the path of your choice of text editor")  # path to notepad ++.
    pe = pefile.PE(exe_path) #

    for section in pe.sections: #list the sections
        print(section.Name.decode('utf-8'))
        print("\tVirtual Address: " + hex(section.VirtualAddress))
        print("\tVirtual Size " + hex(section.Misc_VirtualSize))
        print("\tRaw Size: " + hex(section.SizeOfRawData))


    print(pe.sections[0]) #prints the data from sections

extract()

