f = open("Test02.txt",'r',encoding="UTF-8")
dict = {}
for i in f:
    i = i.replace('\n','')
    a = i.split(":")
    if len(a)==2:
        dict.update({a[0]:a[1]})
f.close()
print(dict)
