li1=[10,20,30,40]
li2=[12,13,14,15]
print(len(li1))
print(len(li2))
if len(li1)==len(li2):
    print("The length of the lists are same")
else:
    print("The length of the lists are not same")
print(sum(li1))
print(sum(li2))
if sum(li1)==(li2):
    print("sum is same")
else:
    print("sum is not same")
if any(value in li2 for value in li1):
    print("There is atleast one common value:")
else:
    print("No common values found")
common_values=[]
for item in li1:
    if item in li2 and item not in common_values:
        common_values.append(item)
print("common_values",common_values)
