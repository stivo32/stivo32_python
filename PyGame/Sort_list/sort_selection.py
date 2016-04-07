# coding=utf-8
#сортировка выбором
def sortSelection(list):

    for curPosition in range(len(list)-1):
        min = list[curPosition]
        minIndex = curPosition
        for scanPosition in range(curPosition+1, len(list)):
            if list[scanPosition] < min:
                min = list[scanPosition]
                minIndex = scanPosition

        if minIndex > curPosition:
            temp = list[minIndex]
            list[minIndex] = list[curPosition]
            list[curPosition] = temp
    return list

list = [10,1,5,7,3,0,125,8,9,33,5,3,23,98]

print(sortSelection(list))