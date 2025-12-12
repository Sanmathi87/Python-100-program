a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=input("Enter the operation +,-,/,*:")
print("The result is:",end='')
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='/':
    print(a/b)
elif c=='*':
    print(a*b)
else:
    print("Error:Wrong operator entered")

Output:
Enter 1st number:45
Enter 2nd number:300
Enter the operation +,-,/,*:*
The result is:13500    

