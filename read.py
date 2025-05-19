import tkinter

root = tkinter.Tk()


file = open("test.txt","r", encoding="UTF-8")
strFile = file.readline()
root.geometry(strFile[:-1])

strFile = file.readline()
root.title(strFile[:-1])

file.close()

root.mainloop()

'''
while True:
    str=file.readline()
    print(str,end="")
    if(str == ""):
        break
'''
'''
fileList = file.readlines()
index = 1
for str1 in fileList:
    print(str(index) + " : " + str1,end='')
    index = index+1
'''