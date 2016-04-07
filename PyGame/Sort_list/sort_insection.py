# coding=utf-8
#сортировка вставками

def sortInsection(list):
    for curPos in range(1, len(list)):
        key = list[curPos]
        scanPos = curPos - 1

        while (scanPos>=0) and (list[scanPos] > key):
            list[scanPos+1] = list[scanPos]
            scanPos -= 1

        list[scanPos+1] = key
    return list

list = [10,1,5,7,3,0,125,8,9,33,5,3,23,98]

print(sortInsection(list))
