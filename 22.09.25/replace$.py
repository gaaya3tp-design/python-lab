s = input("Enter a string: ")
firstchar =s[0]
result = firstchar+s[1:].replace(firstchar, '$')
print(result)
