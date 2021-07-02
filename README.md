# VREproject

import pefile

exe_path = "/home/camrynw28/Downloads/npp.8.1.Installer(2).exe"
pe = pefile.PE(exe_path)

print("[*] Listing imported DLLs...")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print('\t' + entry.dll.decode('utf-8'))

import pefile
exe_path = "/home/camrynw28/Downloads/npp.8.1.Installer(2).exe"
pe = pefile.PE(exe_path)

for entry in pe.DIRECTORY_ENTRY_IMPORT:
    dll_name = entry.dll.decode('utf-8')
    if dll_name == "KERNEL32.dll":
        print("[*] Kernel32.dll imports:")
        for func in entry.imports:
            print("\t%s at 0x%08x" % (func.name.decode('utf-8'), func.address))
