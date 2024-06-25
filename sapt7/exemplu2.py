# Lista de fructe
fructe = ['mar', 'banana', 'mar', 'portocala', 'banana', 'mar']

# Apelăm funcția pentru a număra fructele
rezultat = numara_fructe(fructe)

# Afișăm rezultatul
for fruct, numar in rezultat.items():
    print(f"Ai {numar} {fruct}(e).")
