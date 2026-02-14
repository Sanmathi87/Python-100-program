emp_details=(
    ("EmpId",input("Enter the ID:")),
    ("EmpName",input("Enter the name:")),
    ("EmpAge",input("Enter the age:")),
    ("EmpCity",input("Enter the city:"))
    )

emp=dict(emp_details)
print("\nDictionaries:",emp)
print("Employee name:",emp["EmpName"])
print("Employee city:",emp["EmpCity"])

print("\nKeys:",emp.keys())
print("Values:",emp.values())

emp["phno"]=int(input("Enter the phone number:"))
emp["EmpName"]=input("Enter new employee name:")
emp.pop("EmpAge")

print("\nUpdated Dict:",emp)

print("Length of the dictionary:",len(emp))
emp2=emp.copy()
print("New Dict:",emp2)

emp.clear()
print("\nCleared Dict:",emp)
