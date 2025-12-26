n=int(input("Enter the limit"))
if n%2==0:
      for i in range(n-1,0,-2):
          print(i)
else:
    for i in range(n,0,-2):
        print(i)

Output:
Enter the limit30
29
27
25
23
21
19
17
15
13
11
9
7
5
3
1    
