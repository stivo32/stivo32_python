# coding=utf-8

file = open("example_sorted_names.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()

# for i in name_list:
#     print(i)
#
# i = 0
#
# while i < len(name_list) and name_list[i] != "stivo12":
#     i += 1
#
# if i == len(name_list):
#      print("Имя не найдено")
# else:
#      print("Имя находится в ячейке", i)


list = [x for x in range(0,100)]
print(list)
#бинарный поиск
desired_element = 14
lower_bound = 0
upper_bound = len(list)-1
middle_pos = 0
found = False
while lower_bound < upper_bound and found is False:
    middle_pos = (int) ((lower_bound+upper_bound)/2)
    if list[middle_pos] < desired_element:
        lower_bound = middle_pos+1
    elif list[middle_pos] > desired_element:
        upper_bound = middle_pos
    else:
        found = True

if found:
    print("Имя находится в ячейке", middle_pos)
else:
    print("имя не найдено в списке")



