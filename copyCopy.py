#test.txt파일을 읽어와서
#outTest.py에 
inFile = open("test.txt","r", encoding="UTF-8")
outFile = open("outTest.txt","w", encoding="UTF-8")

while True:
    inStr = inFile.readline()
    inStrChange = ""
    for ch in inStr:
        chNum = ord(ch)
        chNum = chNum + 100
        chChange = chr(chNum)
        inStrChange += chChange
    if(inFile == ''):
        break
    outFile.writelines(inStr)

inFile.close()
outFile.close()