import pefile

def run():
    exe_path = r"C:/Users/wilso/Downloads/npp.8.1.1.Installer.exe" # path for notepad ++
    pe = pefile.PE(exe_path) #

    print("[*] Listing imported DLLs...") # print for data list section
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print('\t' + entry.dll.decode('utf-8'))

    try:
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            print(hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name.decode('utf-8'))
    except:
        print("The exports do not exist")
run()




