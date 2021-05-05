name=input("Enter your name: ")
age=int(input("Enter your age: "))

if name=='Abhiroop':
    print('Hi Abhiroop')
elif age<24:
    print("You're 24")
elif age>2000:
    print("You're a wizard")
elif age>100:
    print("No way, grandpa")
    
    
while True:
    print('Please type your name: ')
    name=input()
    if name=='Abhiroop':
        break
print('Thank You') 
#The print statement above is not indented because the "break" clause closes the loop. 
#Execution moves out of the loop to print "Thank You"