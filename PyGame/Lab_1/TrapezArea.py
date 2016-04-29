while True:
    try:
        h = int(input('Enter the height of the trapezoid:'))
        x1 = int(input('Enter the length of the bottom base:'))
        x2 = int(input('Enter the length of the top base:'))
        break
    except:
        print('Please use only degrees')

area = 0.5*(x1+x2)*h
print("The area is:", area)
