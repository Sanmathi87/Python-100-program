emp1 = {'EmpID': 'E101','EmpName': 'Ravi','EmpAge': 30}

print("\nEmployee Dictionary:", emp1)
print("\nEmployee ID:", emp1['EmpID'])
print("\nEmployee Name:", emp1['EmpName'])


print("\nAll keys in Employee Dictionary:")
for key in emp1:
    print(key)


print("\nAll values in Employee Dictionary:")
for key in emp1:
    print(emp1[key])

# Adding a new employee detail (Email)
emp1["EmpEmail"] = "ravi@example.com"
print("\nUpdated Employee Dictionary (Added Email):", emp1)

# Updating Employee Name
emp1["EmpName"] = "Ramesh"
print("\nUpdated Employee Dictionary (Changed Name):", emp1)

# Deleting Employee Age
emp1.pop("EmpAge")
print("\nUpdated Employee Dictionary (Removed Age):", emp1)

# Length of Dictionary
print("\nNumber of details in Employee Dictionary:", len(emp1))

# Copying Dictionary
emp2 = emp1.copy()
print("\nNew Employee Dictionary (Copy):", emp2)

# Clearing Original Dictionary
emp1.clear()
print("\nOriginal Employee Dictionary after clear:", emp1)
