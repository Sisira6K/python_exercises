a= int(input("Please enter the value of a: "))
b= int(input("Please enter the value of b: "))
c= int(input("Please enter the value of c: "))
d= b**2 -(4*a*c)
if d==0 :
    print("The quadratic equation has exactly 1 real solution.")
elif d>0 :
    print("The quadratic equation has 2 real solutions.")
else :
    print("The quadratic equation has 2 complex solutions.")
