import pefile

exe_path = "/home/cherithkay/Downloads/npp.8.1.Installer.exe"
pe =pefile.PE(exe_path)

for section in pe.sections:
    print(section.Name.decode('utf-8'))
    print("\tVirtual Address: " + hex(section.VirtualAddress))
    print("\tVirtual Size " + hex(section.Misc_VirtualSize))
    print("\tRaw Size: "+ hex(section.SizeOfRawData))

    import pefile

    exe_path = "/home/cherithkay/Downloads/npp.8.1.Installer.exe"
    pe = pefile.PE(exe_path)

    print(pe.sections[0])


