def adauga_carte(fisier, titlu, autor, an):
    with open(fisier, 'a') as f:
        f.write(f"{titlu},{autor},{an}\n")

def afiseaza_carti(fisier):
    try:
        with open(fisier, 'r') as f:
            carti = f.readlines()
            if not carti:
                print("Nu există cărți în bibliotecă.")
            for index, carte in enumerate(carti, 1):
                titlu, autor, an = carte.strip().split(',')
                print(f"{index}. \"{titlu}\" de {autor}, publicată în {an}")
    except FileNotFoundError:
        print("Nu există cărți în bibliotecă.")

def cauta_carte(fisier, titlu_cautat):
    try:
        with open(fisier, 'r') as f:
            carti = f.readlines()
            for carte in carti:
                titlu, autor, an = carte.strip().split(',')
                if titlu.lower() == titlu_cautat.lower():
                    print(f"Cartea găsită: \"{titlu}\" de {autor}, publicată în {an}")
                    return
            print("Cartea nu a fost găsită.")
    except FileNotFoundError:
        print("Nu există cărți în bibliotecă.")

def meniu():
    fisier = 'biblioteca.txt'
    while True:
        print("\nBine ai venit la sistemul de gestiune a bibliotecii!")
        print("Te rog alege o opțiune:")
        print("1. Adaugă o carte")
        print("2. Afișează toate cărțile")
        print("3. Caută o carte")
        print("4. Ieșire")
        
        alegere = input("Alegerea ta: ")
        
        if alegere == '1':
            titlu = input("Introduce titlul cărții: ")
            autor = input("Introduce autorul cărții: ")
            an = input("Introduce anul de publicare: ")
            adauga_carte(fisier, titlu, autor, an)
            print("Cartea a fost adăugată cu succes!")
        elif alegere == '2':
            afiseaza_carti(fisier)
        elif alegere == '3':
            titlu_cautat = input("Introduce titlul cărții pe care vrei să o cauți: ")
            cauta_carte(fisier, titlu_cautat)
        elif alegere == '4':
            print("La revedere!")
            break
        else:
            print("Alegere invalidă, te rog încearcă din nou.")

# Start the program
meniu()
