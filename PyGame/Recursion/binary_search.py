def binary_search_nonrecursive(search_list,key):
    lower_bound = 0
    upper_bound = len(search_list)-1
    found = False
    while lower_bound < upper_bound and found == False:
        middle_pos = (int) ((lower_bound+upper_bound) / 2)
        if search_list[middle_pos] < key:
            lower_bound = middle_pos+1
        elif list[middle_pos] > key:
            upper_bound = middle_pos
        else:
            found = True

    if found:
        print( "The name is at position",middle_pos)
    else:
        print( "The name was not in the list." )

def binary_search_recursive(search_list,key, lower_bound, upper_bound):
    middle_pos = (int) ((lower_bound+upper_bound) / 2)
    if search_list[middle_pos] < key:
        binary_search_recursive(search_list,key, middle_pos+1, upper_bound)
    elif search_list[middle_pos] > key:
        binary_search_recursive(search_list,key, lower_bound, middle_pos )
    else:
        print("Found at position",middle_pos)


file = open('name_list.txt', 'r')
str = file.readline()
name_list = []
while str:
    name_list.append(str.strip())
    str = file.readline()
file.close()
lower_bound = 0
upper_bound = len(name_list)-1
print(name_list)
print(lower_bound, upper_bound)
#binary_search_recursive(name_list,"Morgiana the Shrew",lower_bound,upper_bound)

binary_search_nonrecursive(name_list,"Morgiana the Shrew")
