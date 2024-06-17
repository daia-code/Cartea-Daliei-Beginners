# Funcția pentru calcularea sumei a două numere
def suma(a, b):
    # Returnează suma lui a și b
    return a + b

# Funcția pentru verificarea dacă un număr este par
def este_par(numar):
    # Returnează True dacă numărul este par, altfel False
    return numar % 2 == 0

# Funcția pentru calcularea sumei numerelor de la 1 la n
def suma_pana_la(n):
    suma = 0
    # Buclează de la 1 la n și adaugă fiecare număr la sumă
    for i in range(1, n + 1):
        suma += i
    # Returnează suma calculată
    return suma

# Solicită utilizatorului să introducă două numere
numar1 = int(input("Introdu primul număr: "))
numar2 = int(input("Introdu al doilea număr: "))

# Calculează și afișează suma celor două numere
rezultat = suma(numar1, numar2)
print(f"Suma dintre {numar1} și {numar2} este {rezultat}.")

# Solicită utilizatorului să introducă un număr pentru verificarea parității
numar = int(input("Introdu un număr: "))

# Verifică și afișează dacă numărul este par sau impar
if este_par(numar):
    print(f"Numărul {numar} este par.")
else:
    print(f"Numărul {numar} este impar.")

# Afișează numerele de la 1 la 10
print("Numerele de la 1 la 10 sunt:")
for i in range(1, 11):
    print(i)

# Listă de numere pentru calcularea sumei
numere = [1, 2, 3, 4, 5]
suma_numerelor = 0

# Calculează suma numerelor din listă
for numar in numere:
    suma_numerelor += numar

# Afișează suma numerelor din listă
print(f"Suma numerelor din listă este {suma_numerelor}.")

# Solicită utilizatorului să introducă un număr pentru calcularea sumei până la acel număr
numar = int(input("Introdu un număr pentru a calcula suma numerelor de la 1 până la acel număr: "))
rezultat = suma_pana_la(numar)
print(f"Suma numerelor de la 1 la {numar} este {rezultat}.")

# Verifică și afișează dacă fiecare număr din listă este par sau impar
print("Verificarea parității numerelor din listă:")
for numar in numere:
    if este_par(numar):
        print(f"Numărul {numar} este par.")
    else:
        print(f"Numărul {numar} este impar.")
