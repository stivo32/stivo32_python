import random
for i in range(10):
    x = random.randrange(100000)
    print("{:6,}".format(x))

x=5
y=66
z=777
print("C - '{2} A - '{0}' B - '{1}' C again - '{2}'".format(x,y,z))

my_fruit = ["Apples","Oranges","Grapes","Pears"]
my_calories = [4,300,70,30]

for i in range(4):
    print("{:7} are {:3} calories.".format(my_fruit[i],my_calories[i]) )

for i in range(4):
    print("{:>7} are {:<3} calories.".format(my_fruit[i],my_calories[i]) )

#fill spaces with zero
for hours in range(1,3):
    for minutes in range(0,5):
        print( "Time {:02}:{:02}".format(hours, minutes) )

x=0.1
y=123.456789
print( "{:.1}  {:.1}".format(x,y) )
print( "{:.2}  {:.2}".format(x,y) )
print( "{:.3}  {:.3}".format(x,y) )
print( "{:.4}  {:.4}".format(x,y) )
print( "{:.5}  {:.5}".format(x,y) )
print( "{:.6}  {:.6}".format(x,y) )
print()
print( "{:.1f}  {:.1f}".format(x,y) )
print( "{:.2f}  {:.2f}".format(x,y) )
print( "{:.3f}  {:.3f}".format(x,y) )
print( "{:.4f}  {:.4f}".format(x,y) )
print( "{:.5f}  {:.5f}".format(x,y) )
print( "{:.6f}  {:.6f}".format(x,y) )


x=1234.5678
print( round(x,2) )
print( round(x,1) )
print( round(x,0) )
print( round(x,-1) )
print( round(x,-2) )