book={}
book['tom']={
    'name':'tom',
    'address':'1 ELM Street',
    'number': 90909382302
}

book['james']={
    'name':'james',
    'address':'2 Fleet Street',
    'number': 9043572638
}

import json
s=json.dumps(book)  #dumps 's' stands for string, by dumping, it is converted into a json format. 

print(s)

with open("book.txt",'w') as f:
    f.write(s)
