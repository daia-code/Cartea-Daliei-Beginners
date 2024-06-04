# L=[20,'Jessa',35.75,[30,60,90]] # 0  1 2 3
# # lista = [] are valori
# print(L)
# print(L[3][1]) # lista noastra este pe poz 3 iar elem nostru este pe poz 1

# lista=[20,32,13] # versiune initiala
# lista.append(10)  #versiune noua 
# print(lista) # [20,32,13,10]

# lista=[20,32,13] # versiune initiala
# lista.insert(1,10)  #versiune noua conform pozitiei , 10 vine inaintea lui 32(1)
# print(lista) # [20,10,32,13,10]

# lista=[20,32,13] # versiune initiala
# lista.pop(0) # stergerea pozitiei 0 ( adica a elementului de pe poz 0)
# print(lista) # [32,13]

# liste de siruri de caractere :

# l = ["apple", "banana", "orange", "blueberries"]

# # liste de numere :

# l1 = [3, 4, 8, 1, 7, 2]

# # liste mixte :

# l2 = ["apple", 2, "banana", 8]

# # Cum accesam elementele unei liste :

# print(l[0], l[1], l[2])

# # Functia print poate primi mai mult de un parametru

# # Folosind bucla while

# i=0
# while i < 3:

#     print(l[i])
#     i+=1


 #Un exemplu cu o lista mai mare de elemente

my_list = [23, "abc", 7, "def", 42, "ghi", 12, "jkl", 55, "mno", 18, "pqr", 34, "stu", 91,

    "vwx", 2, "yzs", 8, "abc", 63, "def", 9, "ghi", 1, "jkl", 77, "mno", 29, "pqr", 46, 

    "stu", 13, "vwx", 88, "yzs", 24, "abc", 71, "def",  39, "ghi", 5, "jkl", 68, "mno", 17, 

    "pqr", 52, "stu", 96, "vwx", 31, "yzs", 57, "abc", 84, "def", 22, "ghi", 48, "jkl", 89, 

    "mno", 35, "pqr", 70, "stu", 16, "vwx", 73, "yzs", 30, "abc", 62, "def", 11, "ghi", 95, 

    "jkl", 28, "mno", 53, "pqr", 79, "stu", 43, "vwx", 67, "yzs", 14, "abc", 61, "def", 21, 

    "ghi", 75, "jkl", 38, "mno", 83, "pqr", 44, "stu", 99, "vwx", 50, "yzs", 66, "abc", 25,

    "def", 72, "ghi", 19, "jkl", 60, "mno", 87, "pqr", 36, "stu", 98, "vwx", 45, "yzs"]

i = 0

L = len(my_list) # calculeaza marimea listei / cate elem are lista

print("Nr elemente lista "+str(L))
while i < L:

    print(my_list[i])

    i = i + 1
  # lista=[] # definire lista

# elem=int(input("Introdu un numar:"))

# while elem!=0: # elem diferit de 0
#     lista.append(elem)
#     elem=int(input("Introdu un numar:"))


# print("Ai introdus valoarea 0")
# print(lista)

lista2=[]
caracter=input("Introdu un carcter:") # '' " "
while caracter!='o':
    lista2.append(caracter)
    caracter=input("Introdu un caracter:")
print(lista2)
