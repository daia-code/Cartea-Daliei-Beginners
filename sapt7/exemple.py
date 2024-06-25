#Intercalare

def interleave_multiple_lists(list1,list2):

    result = []

    for a in range(0, len(list1)):

        result.append(list1[a])

        result.append(list2[a])

    return result

list1 = [1,2,3,4,5,6,7]

list2 = [10,20,30,40,50,60,70]

print(interleave_multiple_lists(list1,list2))

#Elemente comune
def find_intersection(my_list, nested_lists):

    big_list = []

    for nested_list in nested_lists:

        intersection = []

        for num in nested_list :

            if num in my_list :

                intersection.append(num)

        big_list.append(intersection)

    return big_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

nested_lists = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

intersections = find_intersection(my_list, nested_lists)

print(intersections)


#Eliminare
def remove_words(in_list, char_list):

    new_list = []

    for line in in_list:

        clean_word = ""

        for l in line :

            if l not in char_list :

                clean_word += l

        new_list.append(clean_word)

    return new_list

str_list = ['Red color', 'Orange#', 'Green', 'Orange @', "White"]

char_list = ['#', 'color', '@']

print(char_list)

print(remove_words(str_list, char_list))
