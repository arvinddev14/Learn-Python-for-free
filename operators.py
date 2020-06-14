a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b) #single slash will provide value with decimal value
print(a // b) #double slash will provide value with no decimal value
print(a % b) #the remainder after integer division

print()
for i in range(1 , a // b):
    print(i)

print(a + b / 3 - 4 * 12) #Division,multiplication and then add and sub . If  sub precludes with multiplocation,then value is negative and then follow  rest of math operator precedence.
print(a + (b / 3) - (4 * 12))
print((((a+b)/3)-4)*12)
print(((a+b)/3-4)*12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) / b)
