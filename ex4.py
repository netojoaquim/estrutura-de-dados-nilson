lista=[1,3,2,8,7,4,4,25,8,69,80]
lista2=[]
for i in lista:
    if i %2==0:
        lista2.append(i)
print(f"LISTA ORDENADA:{sorted(lista2)}")