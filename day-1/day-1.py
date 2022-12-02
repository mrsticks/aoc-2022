f = open("./input", 'rb')
#elves-cals=[]

for line in f:
    cals=0
    
    if not ('\r\n' in line):
        print(type(int(line.strip())))
    else:
        pass

    cals=0
f.close()
