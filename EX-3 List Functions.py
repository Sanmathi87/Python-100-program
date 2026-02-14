num=[2,56,89,90,55]
print("Original:",num)
num.append(60)
num.insert(2,67)
num.remove(89)
num.pop(0)
print("Modified:",num)

#Sort()
num.sort()
print("Sorted:",num)

#reverse()
num.reverse()
print("Reverse:",num)

print("length:",len(num))
print("Max:",max(num))
print("Min:",min(num))
print("Sum:",sum(num))

#copy()
new_list=num.copy()
print("new list:",new_list)

#clear()
num.clear()
print("Cleared list:",num)
