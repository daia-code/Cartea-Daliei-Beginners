import random

def ghiceste_numarul():
    numar_secret = random.randint(1, 100)
    incercari_maxime = 10

    print("Bine ai venit la jocul 'Ghicește numărul'!")
    print(f"Am ales un număr între 1 și 100. Încearcă să-l ghicești în maxim {incercari_maxime} încercări.")

    for incercari in range(1, incercari_maxime + 1):
        numar_ghicit = int(input(f"Încercarea {incercari}: Introdu numărul tău: "))

        if numar_ghicit < numar_secret:
            print("Prea mic! Încearcă din nou.")
        elif numar_ghicit > numar_secret:
            print("Prea mare! Încearcă din nou.")
        else:
            print(f"Felicitări! Ai ghicit numărul {numar_secret} în {incercari} încercări.")
            break
    else:
        print(f"Îmi pare rău, ai epuizat toate {incercari_maxime} încercări. Numărul secret era {numar_secret}.")

# Pornirea jocului
ghiceste_numarul()
