dict1={'StdNo':'532','StuName':'Naveen','StuAge':21,'StuCity':'Hyderabad'}
print("\nDictionary is:",dict1)

print("\nStudent Name is:",dict1['StuName'])
print("\nStudent City is:",dict1['StuCity'])

print("\nAll keys in Dictionary")
for x in dict1:
    print(x)
    
print("\nAll Values in Dictionary")
for x in dict1:
    print(dict1[x])
    
dict1["Phno"]=85457854
print("\nUpdated Dictionary is:",dict1)

dict1["StuName"]="Madhu"
print("\nUpdated Dictionary is:",dict1)

dict1.pop("StuAge");
print("\nUpdated Dictionary is:",dict1)

print("Length of Dictionary is:",len(dict1))

dict2=dict1.copy()
print("\nNew Dictionary is:",dict2)

dict1.clear()
print("\nUpdated Dictionary is:",dict1)
    
