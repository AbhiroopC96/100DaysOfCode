x=input('Enter a number:')
y=input("Enter a number:")

try:
    z=x/int(y)
except ZeroDivisionError as e:
    z=None
except Exception as e:
    print("Exception is:",type(e).__name__)
    z=None
    print("Division is:",z)