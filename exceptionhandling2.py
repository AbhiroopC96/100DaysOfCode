x=input("Enter a number:")
y=input("Enter a number:")

try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    z=None
print("Division is:",z)