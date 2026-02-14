file=r"C:\Users\sanma\OneDrive\Documents\Python\Sample (2).txt"

with open(file,"w") as f:
    f.write("Python is easy to learn\n")
    f.write("File handling is very important\n")

with open(file,"a") as f:
    f.write("Pratice makes a person perfect\n")

with open(file,"r") as f:
    text=f.read()

print("File content:",text)
print("Lines:",text.count("\n"))
print("Words:",len(text.split()))
print("characters:",len(text))
print("Python count:",text.count("Python"))      
