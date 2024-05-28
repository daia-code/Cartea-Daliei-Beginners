text='Abecedar'
text2="Abecedar"
litera='a'
litera2="a"
print(text)
print(text2)
print(litera)
print(litera2)
a = input("Cati ani ai? ") 
nume = input("Nume ") 
varsta = input("Varsta ") 

print("Numele meu este" + nume+" si am "+varsta+" ani")
print(f"Numele meu este {nume} si am {varsta} ani")



#Problema : input - numele , varsta, hobby-uri

varsta=22
nume="Mihai"
print("Numele meu este "+nume+str(varsta)+" de ani") # int->string str()
print("Numele meu este ",nume,str(varsta)," de ani") #string "20"->int("20")
print(int("20")) #int->integer/numar
print(20)

# numar1=input()
# numar2=input()
# if numar1>numar2: # < >
#     print(numar1)
# print(numar1<=numar2) # == < > 

'''
Verificați dacă un număr este mai mare decât celălalt.

Dacă sunt, afișează diferența numerelor.

Altfel dacă numărul este mai mic decât celălalt, afișează suma numerelor.

Altfel afișează șirul de caractere „numerele sunt egale”.
'''


# numar=str(input()) # input()- citire de la tastatura
# print(10+numar)

vreau_sa_numar=10
numar_initial=0

while numar_initial<=vreau_sa_numar:
    print(numar_initial)
    numar_initial=numar_initial+1 # 1

varsta=18
drept_Vot=True

while varsta==18 and drept_Vot==True: # cat timp varsta==18 si drept_vot este true
    print("Veti vota")
    varsta=varsta-1
print("Nu mai poti vota")
