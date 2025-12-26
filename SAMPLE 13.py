n=int(input("Enter the limit less than 99999999999 "))
small=99999999999
for i in range(1,n+1):
    print("Enter ",i,end='')
    a=int(input("th number:"))
    if a<small:
        small=a
print("Smallest no.is :",small)        

Output:
Enter the limit less than 99999999999 2
Enter  1th number:3
Enter  2th number:4
Smallest no.is : 3    
