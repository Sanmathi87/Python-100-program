name=input("enter name:")
roll=input("enter roll number:")
course=input("Course name:")
print("\nEnter marks out of 100:\n")
s1=int(input("subject 1:"))
s2=int(input("subject 2:"))
total=s1+s2
percentage=total/2

if percentage>=90:
       grade="A"
elif percentage>=80:
    grade="B"
elif percentage>=70:
    grade="C"    
elif percentage>=60:
    grade="D"
else:
    grade="Fail"


print("\nSTUDENT MARKS\n")
print("Name:",name)
print("Roll number:",roll)
print("Course:",course)
print("Total marks:",total)
print("Percentage:",percentage)
print("Grade:",grade)
