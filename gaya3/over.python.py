a=input("Enter integers separated by spaces: ")
numbers = a.split()
result = []
for num in numbers:
    n = int(num)
    if n > 100:
        result.append("over")
    else:
        result.append(n)

print(result)
