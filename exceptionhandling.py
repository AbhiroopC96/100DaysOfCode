x= input("Enter a number:")
y=input("Enter a number:")

try:
    z=int(x)/int(y)
except Exception as e:
    z=None
print("Division is:",z)


# Exception handling avoids the code from failing to run. 

