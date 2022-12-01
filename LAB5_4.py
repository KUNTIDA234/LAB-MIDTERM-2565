filename = "Test01.txt"
f = open(filename,'w')
myInput = ""
myInput = input("Enter Line ('\\' to exit):")
while myInput != "\\":
    print(myInput)
    f.write(f"{myInput}\n")
    myInput = input("Enter Line ('\exit'to exit):")
print("End")
f.close()
