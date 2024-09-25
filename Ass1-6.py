a=int(input("Enter first number : ")) 
b=int(input("Enter second number : ")) 
print("The sum is : ",a+b) 
print("The subtracion is : ",a-b) 
print("The muliplication is : ",a*b) 
print("The float division is : ",a/b) 
print("The integer division is : ",a//b) 
print("The modulo division is : ",a%b) 
print("The to the power is : ",a**b
#--------------      -------------------------#
  year=int(input("Enter a year : ")) 
if(year%400==0): 
 print(year,"is a century leap year") 
elif(year%100==0): 
 print(year,"is a century year") 
elif(year%4==0): 
 print(year,"is a leap year") 
else: 
 print(year,"is not a century or not a leap year")
#---------------------------#

x=int(input("Enter the first side of the triangle : ")) 
y=int(input("Enter the second side of the triangle : ")) 
z=int(input("Enter the third side of the triangle : ")) 
if(x+y>z and y+z>x and x+z>y): 
 print("This is a triangle") 
 if(x==y==z): 
 print("This is an Equilateral triangle") 
 elif(x==y or y==z or z==x): 
 print("This is an Isosceles triangle") 
 else: 
 print("This is a Scanlene triangle") 
else: 
 print("This is not a triangle")
#-----------------------------------#
angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

if angle1 + angle2 + angle3 != 180:
  print("Not a triangle")
else:
    if angle3 > 90:
        print("Obtuseangle triangle")
    elif angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Rightangle triangle")
    else:
        print("Acute angle triangle")
#-------------------------#
base=float(input("Enter the base of the triangle : ")) 
height=float(input("Enter the height of the triangle : ")) 
print("The area of the triangle is : ",0.5*(base*height),"square units")
#------------------------#
import math 
a=float(input("Enter coefficient a : ")) 
b=float(input("Enter coefficient b : ")) 
c=float(input("Enter coefficient c : ")) 
discriminant=b**2-4*a*c 
if(discriminant>0): 
 root1=(-b+math.sqrt(discriminant))/(2*a) 
 root2=(-b-math.sqrt(discriminant))/(2*a) 
 print("The equation has two real roots : ",root1,root2) 
elif(discriminant==0): 
 root=-b/(2*a) 
 print("The equation has one real root : ",root) 
else: 
 real_part=-b/(2*a) 
