lista=[1,3,2,8,7,4,4,25,8,69]
entr=int(input())
cont=0
for i in lista:
    if i==entr:
        cont+=1
print(f"O N° {entr} aparece {cont} vezes")