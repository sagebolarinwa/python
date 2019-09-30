# Read an integer:
# a = int(input())
# Print a value:
# print(a)

a = int(input())
b = (a % 10)
c = (a // 100)
d = (a // 10 % 10)
print(d + b + c)