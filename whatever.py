import re 
iden = "nom"
l =[]
print(iden)
with open("database.txt", mode="rb") as d:
    for line in d.readlines():
        l = [x for x in (line[:2]).split(":")]
        if iden in l[:2]:
            break
print(l[0],l[1],l[2])