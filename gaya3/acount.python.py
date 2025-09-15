names = ["Alice", "Bob", "Amanda", "Charlie", "Anna"]
count_a = 0
for name in names:
    count_a += name.lower().count('a')
print(count_a)
