import pefile
import postgresDatabase

def run(enterpath):
    pe = pefile.PE(enterpath)

    print("[*] Listing imported DLLs...") # print for data list section
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print('\t' + entry.dll.decode('utf-8'))

    try:
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            print(hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name.decode('utf-8'))
    except:
        print("The exports do not exist")

        postgresDatabase.postgres_database()


