def readFile(filename):
    file = open(filename, 'r')
    for name in file:
        print(name)
    file.close()
    
readFile('D:/Day3/names.txt')

def readFile2(filename):
    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line)
readFile2('D:/Day3/names.txt')    
        
def writeFile(filename, data):
    with open(filename, 'w') as file:
        file.write(data + '\n')

writeFile('D:/Day3/names2.txt', "Sathish")
        
def appendFile(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

appendFile('D:/Day3/names3.txt', "Sathish")