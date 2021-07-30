import pefile
import postgresDatabase

def extract(enterpath):
    pe = pefile.PE(enterpath) #
    for section in pe.sections: #list the sections
        print(section.Name.decode('utf-8'))
        print("\tVirtual Address: " + hex(section.VirtualAddress))
        print("\tVirtual Size " + hex(section.Misc_VirtualSize))
        print("\tRaw Size: " + hex(section.SizeOfRawData))


    print(pe.sections[0]) #prints the data from sections

    n=13

    def divide_chunks(l, n):

        for i in range(0, len(l), n):
            yield l[i:i + n]
    x= list(divide_chunks(pe.sections,n))

    print(x)

    postgresDatabase.postgres_database()





