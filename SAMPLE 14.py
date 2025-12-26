a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Second largest element is:",a[n-2])

Output:
Enter number of elements:4
Enter element:3
Enter element:5
Enter element:9
Enter element:8
Second largest element is: 8    
