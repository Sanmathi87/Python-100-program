import re
phone=input("Enter the phone number(XXX-XXX-XXXX):")

if re.match(r"\d{3}-\d{3}-\d{4}",phone):
            print("Vaild phone number")
else:
    print("Invalid phone number")
    
password=input("Enter the password")
if re.match(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}",password):
    print("VAlid password")
else:
    print("Weak password,it should contain:")
    print(" - 1 uppercase")
    print(" - 1 lowercase")
    print(" - 1 digit")
