'''
Scrieți un program care imprimă toate subșirurile care au o lungime de cel puțin trei caractere și care încep cu caracterul specificat de utilizator.

# SAMPLE INPUT/OUTPUT :

# Please type in a word: mammoth

# Please type in a character: m

# mam

# mmo

# mot
'''

x = input("Please type in a word: ")

y = input("Please type in a character: ")

while len(x) >= 3:

    # print("x " + x)

    i = x.find(y)

    if i < 0 :

        break

    elif len(x[i:i+3]) >= 3 :

        print(x[i:i+3])

        x = x[i+1:]

    else :

        break
