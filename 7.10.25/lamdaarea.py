square=lambda side:side*side
rectangle=lambda length,breadth:length*breadth
triangle=lambda base,height:1/2*(base*height)
a=int(input("Enter the side of square:"))
print("Area of square is:",square(a))
b=int(input("Enter the length:"))
c=int(input("Enter the breadth:"))
print("Area of rectangle is:",rectangle(b,c))
d=int(input("Enter the base:"))
e=int(input("Enter the height:"))
print("Area of triangle is:",triangle(d,e))
