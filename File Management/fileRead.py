
try :
    readFile = open("File Management\\FileReadTxtFile.txt",'r') # please use full path insteed of relative path. But testing purposes we can easily use relative path.
    print(readFile.read())
    readFile.close()
except Exception as err:
    print(err)
