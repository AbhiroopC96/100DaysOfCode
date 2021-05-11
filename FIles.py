f=open("C:\\Users\\Abhiroop Chakraborty\\Desktop\\100daysofcode\\book.txt",'r')
f_out=open("C:\\Users\\Abhiroop Chakraborty\\Desktop\\100daysofcode\\book_out.txt",'w')
for line in f:
    tokens=line.split(' ')
    f_out.write(str(tokens)+"wordcount"+str(len(tokens)))
    print(len(tokens))
f.close()

# 'a'-- appends stuff to the file. 
