__author__ = 'k_eryomenko'
"""
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
0
"""
for i in range(10,0,-1):
    for j in range(i):
        print(j, end=" ")
    print()

"""
0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7
      0 1 2 3 4 5 6
        0 1 2 3 4 5
          0 1 2 3 4
            0 1 2 3
              0 1 2
                0 1
                  0
"""
for i in range(10,0,-1):
    print(" "*2*(10-i),end="")
    for j in range(i):
        print(j, end=" ")
    print()

"""
1   2   3   4   5   6   7   8   9
2   4   6   8  10  12  14  16  18
3   6   9  12  15  18  21  24  27
4   8  12  16  20  24  28  32  36
5  10  15  20  25  30  35  40  45
6  12  18  24  30  36  42  48  54
7  14  21  28  35  42  49  56  63
8  16  24  32  40  48  56  64  72
9  18  27  36  45  54  63  72  81
"""
for i in range(1,10):
    for j in range(1,10):
        k = i*j
        if k < 10:
            print("  "+str(k), end=" ")
        else:
            print(" "+str(k), end=" ")
    print()

"""
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
"""
for i in range(1, 10):
    print(" "*2*(10-i), end="")
    for j in range(i):
        print(j+1, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()

"""
                   1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8
      1 2 3 4 5 6 7
        1 2 3 4 5 6
          1 2 3 4 5
            1 2 3 4
              1 2 3
                1 2
                  1
"""
for i in range(1, 10):
    print(" "*2*(10-i), end="")
    for j in range(i):
        print(j+1, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()
for i in range(8,0,-1):
    print(" "*2*(10-i),end="")
    for j in range(i):
        print(j+1, end=" ")
    print()


"""
                   1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8
      1 2 3 4 5 6 7
        1 2 3 4 5 6
          1 2 3 4 5
            1 2 3 4
              1 2 3
                1 2
                  1
"""
for i in range(1, 10):
    print(" "*2*(10-i), end="")
    for j in range(i):
        print(j+1, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()
for i in range(8,0,-1):
    print(" "*2*(10-i),end="")
    for j in range(i):
        print(j+1, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()

