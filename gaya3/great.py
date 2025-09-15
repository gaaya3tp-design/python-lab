a=int(input("Enter First number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a > b and a > c:
    print("a is greatest")
elif b > a and b > c:
    print("b is greatest")
elif c > a and c > b:
    print("c is greatest")
else:
    print("There is a tie")
