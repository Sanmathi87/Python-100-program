import math
a=int(input("Enter a "))
b=int(input("Enter b "))
c=int(input("Enter c "))
d=(b*b)-(4*a*c)
if d>=0:
    print("root are:")
    x1=-b+math.sqrt(d)/(2*a)
    x2=-b-math.sqrt(d)/(2*a)
    print("x1==",x1)
    print("x2==",x2)
else:
    print("root are imaginary.")

Output:
Enter a 23
Enter b 67
Enter c 44
root are:
x1== -66.54347826086956
x2== -67.45652173913044    
    
