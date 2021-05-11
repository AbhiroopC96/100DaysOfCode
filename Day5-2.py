f=open("book.txt",'r')
s=f.read()
print(s)

import json
book=json.loads(s)  #loads 's' -- loads the JSON string
print(book['james'])

print(book['james']['address'])