while True:
    try:
        farDegree = float(input('Enter temperature in Fahrenheit:'))
        break
    except:
        print('Enter temperature with degrees')

celDegree = (farDegree-32)/1.8
print('The temperature in Celsius:', celDegree)
