print("Hello World!!!!! fuckin java")
print(10/3)
print(10//3)
a = 12
if a>13 :
    print("でっかい")
else :
    print("ちっさい")

i=0
while i<3 : 
    print("これは",i,"回目(while)")
    i += 1

for i in range(3):
    print("これは",i,"かいめ(for)")

list = ["test1",'test2']
for name in list:
    print("nomal"+name)

list.append("test3")

for name in list:
    print("append",name)

list.insert(3,"test4")

for name in list:
    print("insert",name)

del list[0]

for name in list:
    print("del",name)

list.remove("test2")

for name in list:
    print("remove",name)