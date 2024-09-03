fileRead = open("File Management\\FileReadTxtFile.txt",'r')
fileReadData = fileRead.read()
fileRead.close()

fileWrite = open("File Management\\filedataStore.txt",'w')
fileWrite.write(fileReadData)
fileWrite.close()