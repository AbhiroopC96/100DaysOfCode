exp=[2400,2000,1500,2000,1200]
#for x in exp:
 #   print(sum(x)) This does not work as int object is not iterable. 
total=0
for x in exp:
    total+=x 
print(total)

exp=[2400,2000,1500,2000,1200]
total=0
for i in range(len(exp)):
    print('Month',(i+1),'Expense',exp[i])
    total+=exp[i]
print('Total Expense: ',total)

key_location='chair'
locations=['table','bed','chair','closet']

for i in locations:
    if i==key_location:
        print('Key is found: ',i)
        break  ##The break function- Does not continue looping once funtion is complete. 
    else:
        print('Key is not found: ',i)

for i in range(1,6):
    if i%2==0:
        continue  ##The continue function- sends it back to the start of the loop and does not print anything else in the loop. 
    else:
        print(i*i)


toms_exp=[2000,3000,1000]
joes_exp=[3000,1000,2000]

def calculate(exp):
    total=0
    for i in exp:
        total+=i
    print(total)

toms_total=calculate(toms_exp)
print(toms_total)