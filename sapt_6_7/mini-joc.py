import random

# Funcția pentru calcularea sumei a două numere
def suma(a, b):
    return a + b

# Funcția pentru verificarea dacă un număr este par
def este_par(numar):
    return numar % 2 == 0

# Funcția pentru calcularea sumei numerelor de la 1 la n
def suma_pana_la(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Funcția principală pentru mini joc
def mini_joc():
    scor = 0

    print("Bine ai venit la mini jocul matematic!")
    print("Vei primi 5 întrebări. Răspunde corect pentru a câștiga puncte.\n")

    # Întrebarea 1: Adunare simplă
    numar1 = random.randint(1, 10)
    numar2 = random.randint(1, 10)
    raspuns_corect = suma(numar1, numar2)
    raspuns_utilizator = int(input(f"Care este suma dintre {numar1} și {numar2}? "))
    if raspuns_utilizator == raspuns_corect:
        print("Corect!")
        scor += 1
    else:
        print(f"Greșit. Răspunsul corect era {raspuns_corect}.")

    # Întrebarea 2: Verificare paritate
    numar = random.randint(1, 20)
    raspuns_utilizator = input(f"Numărul {numar} este par? (da/nu) ").strip().lower()
    if (raspuns_utilizator == "da" and este_par(numar)) or (raspuns_utilizator == "nu" and not este_par(numar)):
        print("Corect!")
        scor += 1
    else:
        print(f"Greșit. Răspunsul corect era {'da' if este_par(numar) else 'nu'}.")

    # Întrebarea 3: Suma numerelor de la 1 la n
    numar = random.randint(1, 10)
    raspuns_corect = suma_pana_la(numar)
    raspuns_utilizator = int(input(f"Care este suma numerelor de la 1 la {numar}? "))
    if raspuns_utilizator == raspuns_corect:
        print("Corect!")
        scor += 1
    else:
        print(f"Greșit. Răspunsul corect era {raspuns_corect}.")

    # Întrebarea 4: Afișare numere de la 1 la 5
    print("Numerele de la 1 la 5 sunt:")
    for i in range(1, 6):
        print(i)

    # Întrebarea 5: Verificare paritate pentru fiecare număr dintr-o listă
    numere = [1, 2, 3, 4, 5]
    print("Verifică dacă numerele din listă sunt pare sau impare:")
    for numar in numere:
        raspuns_utilizator = input(f"Numărul {numar} este par? (da/nu) ").strip().lower()
        if (raspuns_utilizator == "da" and este_par(numar)) or (raspuns_utilizator == "nu" and not este_par(numar)):
            print("Corect!")
            scor += 1
        else:
            print(f"Greșit. Răspunsul corect era {'da' if este_par(numar) else 'nu'}.")

    # Afișarea scorului final
    print(f"\nJocul s-a terminat! Scorul tău final este: {scor} din 5.")

# Pornirea mini jocului
mini_joc()
