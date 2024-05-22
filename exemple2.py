'''
Suntem într-un magazine si vrem sa ne cumparam un laptop, o console de jocuri,
 o pereche de căști și un mouse. Calculati  pretul total in urma achiziției si 
 dacă ati reusit sa luati tot ce aveați pe listă 
'''
# produse disponibile
laptop=True
console_Game=False
casti=False
mouse=True

# pret produse 
laptop_Pret=4000
console_Game_Pret=2700
casti_Pret=90
mouse_Pret=50

pret_Total=0
produse=0

#verificam daca produsele sunt disponibile
if(laptop==True):
    pret_Total=pret_Total+laptop_Pret
    produse=produse+1
if(console_Game==True):
    pret_Total=pret_Total+console_Game_Pret # se mai poate scrie pret_Total+=console_Game_Pret
    produse=produse+1 # se mai poate scrie produse+=1
if(casti==True):
    pret_Total+=casti_Pret
    produse+=1
if(mouse==True):
    pret_Total+=mouse_Pret
    produse+=1
print("Pentru "+str(produse)+" produse am platit "+str(pret_Total))

#se foloseste elif in cazurile unde se stie ca programul nu respecta conditia de true

#rezolvare problema cu elif
'''
Avem un joben cu 3 bile: 
1 bila rosie
1 bila albastra
1 bila galbena
vreau sa scot doar bila albastra din joben
Cum pot verifica ce am scos?
'''
# in functie de ordinea verificarii condtiitlor din if, daca codul intra in if/elif
# nu mai merge la alta instructiune de if de care apartine if-else if-elif-else
# observati linia 54->59
rosie=True
albastra=False
galbena=True

if(rosie==True):
    print("Am scos bila rosie")
elif(albastra==True):
    print("Am scos bila albastra")
else:
    print("Am scos bila galbena")

#observati linia 62, este independenta de if-elif-else linia 54->59
if(albastra==False):
    print("Bila albastra nu era in joben!")
