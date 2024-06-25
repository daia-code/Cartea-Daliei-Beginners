#1
def afiseaza_dictionar(dictionar):

    for cheie, valuare in dictionar.items():

        if valuare % 2 == 0 :

            print(cheie + ": " + str(valuare))

dictionar = {

    "ana" : 4,

    "george" : 5

}

afiseaza_dictionar(dictionar)


#2

def afiseaza_dictionar(dictionar):

    for cheie, valuare in dictionar.items():

        if len(valuare) > 3 :

            print(cheie + ": " + str(valuare))

dictionar = {

    "Marin" : "Ana",

    "Marinescu" : "George"

}

afiseaza_dictionar(dictionar)


#3 utilizare zip() 
dictionar = {}

def afiseaza_dictionar(dictionar):

    nume = ["Alice", "Bob", "Charlie", "Diana"]

    varste = [25, 30, 22, 28]

    perechi = zip(nume, varste)

    for k, v in perechi :

        dictionar[k] = v

    print(dictionar)

afiseaza_dictionar(dictionar)

#4
nume = ["Andrei", "Maria", "Ion", "Gabriela", "Elena"]

varste = [21, 35, 20, 29, 32]

def creeaza_dictionar(nume, varste) :

    rezultat = {}

    perechi = zip(nume, varste)

    for n, v in perechi:

        if len(n) > 4 and v % 2 == 1:

            rezultat[n] = v

    print(rezultat)

creeaza_dictionar(nume, varste)

#5 insert()
fruits = ["apple", "banana", "grapes"]

fruits.insert(1, "orange")

print(fruits)

#6 stergere articol din dictionar
del dictionary_name[key]

#7
copii_cuminti = ["John", "Jane", "Jim"]

dictionar_dorinte = {

    "John": ["toy car", "Lego set"], 

    "Jane": ["doll", "coloring book"], 

    "Jim": ["football", "basketball"], 

    "Tom": ["skateboard"]

}

for copil in list(dictionar_dorinte.keys()):

    if copil not in copii_cuminti:

        del dictionar_dorinte[copil]

print(dictionar_dorinte)

#8
d = {

    "ana": 5,

    "maria": 6

}

def reversed_dict(d):

    reversed_d = {}

    for key, value in d.items():

        reversed_d[value] = key

    return reversed_d

print (reversed_dict(d))

#9 utilizare split()
sentence = "the cat sat on the mat"

new = sentence.split()

print(new)

#10
text = "Hello World, Hello again World"

words = {}

n = 2

for word in text.split():

    if word in words:

        words[word] += 1

    else:

        words[word] = 1

print("Words count:", words)

for word, count in words.items():

    if count > n:

        print(word, "appears", count, "times")

#11
text = "Hello World"

litere = {}

vocale = "aeiouAEIOU"

for caracter in text:

    if caracter in vocale:

        if "vocale" in litere:

            litere["vocale"] += 1

        else:

            litere["vocale"] = 1

    else:

        if "consoane" in litere:

            litere["consoane"] += 1

        else:

            litere["consoane"] = 1

print("nr de litere:", litere)

for litera, nr in litere.items():

    if nr >= 5:

        print(litera, "appears", nr, "times")

#12 sorted()
a = ("b", "g", "a", "d", "f", "c", "h", "e")

x = sorted(a)

print(x)

#13
color_dict = {'red':'#FF0000',

          'green':'#008000',

          'black':'#000000',

          'white':'#FFFFFF'}

for key in sorted(color_dict):

    print("%s: %s" % (key, color_dict[key]))


#14
student_data = {'id1': 

   {'name': ['Sara'], 

    'class': ['V'], 

    'subject_integration': ['english, math, science']

   },

 'id2': 

  {'name': ['David'], 

    'class': ['V'], 

    'subject_integration': ['english, math, science']

   },

 'id3': 

    {'name': ['Sara'], 

    'class': ['V'], 

    'subject_integration': ['english, math, science']

   },

 'id4': 

   {'name': ['Surya'], 

    'class': ['V'], 

    'subject_integration': ['english, math, science']

   },

}

result = {}

for key,value in student_data.items():

    if value not in result.values():

        result[key] = value

print(result)


#15
dict1 = {"a": 1, "b": 2, "c": 3}

dict2 = {"a": 2, "b": 3, "d": 4}

result = {}

for key in dict1.keys():

    if key in dict2:

        result[key] = dict1[key] + dict2[key]

    else:

        result[key] = dict1[key]

for key in dict2.keys():

    if key not in result:

        result[key] = dict2[key]

print("Result:", result)


#16
d = {"a": [1, 2, 3], "b": [4, 5], "c": [6]}

min_length = float("inf")

shortest_list = []

for key, values in d.items():

    if len(values) < min_length:

        min_length = len(values)

        shortest_list = values

print("Shortest list:", shortest_list)

#17 pop()
marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }

element = marks.pop('Chemistry')

print('Popped Marks:', element)

# Output: Popped Marks: 72


#18
sample_dict = {

  "name": "Kelly",

  "age":25,

  "salary": 8000,

  "city": "New york"

}


sample_dict['location'] = sample_dict.pop('city')

print(sample_dict)


