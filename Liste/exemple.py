'''
Având în vedere lista de mai jos:

my_list= [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]

Tipăriți toate numerele impare din lista.
'''
i = 0

while i < len(my_list):

    if my_list[i] % 2 != 0:

        print(my_list[i])

    i += 1

# ce este i += 1

# forma scurta a expresiei i = i + 1


'''
Având în vedere lista de mai jos: 

my_list = [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16] 

Scrieți un program care returnează cel mai mare număr din listă. 
'''
max = 0

i = 0

while i < len(my_list):

    if my_list[i] > max:

        max =  my_list[i]

    i += 1

print("greatest nr is : ", max)


'''
Scrieți un program care să calculeze media numerelor dintr-o listă.

'''
my_list = [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]

sum_of_numbers = 0

count_of_numbers = 0

i = 0

while i < len(my_list):

    sum_of_numbers += my_list[i]

    count_of_numbers += 1

average = sum_of_numbers / count_of_numbers

print("The average of the numbers you entered is: ", average)



'''
Scrieți un program care preia o listă de numere și returnează o nouă listă care conține numerele în ordine inversă.

'''
my_list = [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]

reverse_list = []

i = len(my_list)-1

j = 0

while i >= 0:

    reverse_list[j] = my_list[i]

    # short form for i = i - 1

    i -= i

print(reverse_list)



'''
Scrieți un program care cere șiruri de caractere de la utilizator până când acesta introduce „stop” 

'''
names = []

user_input = ""

while user_input != "stop":

    user_input = input("Enter a name, or 'stop' to quit: ")

    if user_input == "stop":

        break

    names.append(user_input)

print("The names you entered are: ", names)





'''
Eliminați toate numerele din listă care sunt divizibile cu 3.


'''
my_list = [5, 2, 8, 10, 15, 6, 7, 12, 20]

i = 0

while i < len(my_list):

    if my_list[i] % 3 == 0:

        print(my_list[i])

        my_list.pop(i)

        i -= 1

    i += 1

print(my_list)


# Atenție cu acesta, probabil o să rateze decrementul

# și ajungeți cu o listă care conține 6

# merită să petreceți ceva timp pentru debug, 

# adăugați print i și print my_list[i]

# și trece-ti prin problema pas cu pas
