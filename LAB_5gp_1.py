file = "Test03.txt"
f = open(file,"a",encoding="UTF-8")

while True:
    word = input("Enter String('\\'to exit) : ")
    if word == "\\":
        break
    elif ":" in word:
        print(f"{word} has been added successfully.")
        f.write(f"{word}\n")
    else:
        print("Invalid format !")

dic = {}
with open(file,"r",encoding="UTF-8") as f:
    for i in f:
        (w1,w2) = i.split(":")
        dic[w1] = w2

while True:
    word = input("Enter String to search ('\\') to exit : ")
    if word == "\\":
        break

    if word not in dic:
        print("Can't find this word!")
    else:
        w1 = word
        w2 = dic[w1]
        print(f"{w1} = {w2}")
