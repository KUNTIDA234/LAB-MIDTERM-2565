n = input("Input Number : ")
x = n.split(' ')
for i in range(len(x)):
    count = count + len(x[i])

print(str(count))