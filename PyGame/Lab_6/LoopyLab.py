
'''
10
11 12
13 14 15
16 17 18 19
20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36 37
38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54
'''
count=10
for i in range(0,9):
    for j in range(0,i+1):
        print(count,end=" ")
        count+=1
    print("")


'''
E.g. n = 3
oooooo
o    o
oooooo

E.g. n = 8
oooooooooooooooo
o              o
o              o
o              o
o              o
o              o
o              o
oooooooooooooooo
'''
n = 8
for i in range(n):
    for j in range(n):
        if i==0 or i == (n-1) or j == 0 or j ==(n-1):
            print('o', end=' ')
        else:
            print(' ', end=' ')
    print('')


'''
E.g. n = 3

1 3 5 5 3 1
3 5     5 3
5         5
5         5
3 5     5 3
1 3 5 5 3 1

E.g. n = 5
1 3 5 7 9 9 7 5 3 1
3 5 7 9     9 7 5 3
5 7 9         9 7 5
7 9             9 7
9                 9
9                 9
7 9             9 7
5 7 9         9 7 5
3 5 7 9     9 7 5 3
1 3 5 7 9 9 7 5 3 1
'''

n = 5
numberi = 1
for i in range(0,n):
    numberj=numberi
    for j in range(n-i,0,-1):
        print(numberj,end=' ')
        numberj+=2
    numberj-=2
    if i>0:
        print(" "*i*4, end='')

    for j in range(n-i,0,-1):
        print(numberj,end=' ')
        numberj-=2
    print()
    numberi+=2
numberi-=2
for i in range(0,n):
    numberj=numberi
    for j in range(0, i+1):
        print(numberj, end=' ')
        numberj+=2
    numberj-=2
    if i<(n):
        print(' '*(n-1-i)*4, end='')
    for j in range(0, i+1):
        print(numberj, end=' ')
        numberj-=2
    print()
    numberi-=2