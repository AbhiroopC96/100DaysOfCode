d = {"Tom": 900038832, "Sam": 90440934902,
     "Jamie": 849349938301, "Hal": 4934837382}

print(d["Tom"])

del d["Jamie"]

print(d)

# d.clear--- to remove all the keys and values inside a dictionary

#-------------------------------------Modules----------------------------------------------#

import math

print(math.sqrt(16))
print(math.pow(2, 4))


import functions as f

area = f.area_of_rectangle(9, 7)

print(area)


##### In case the functions are not in the same folder, we have to import the sys module
# import sys
# sys.path.append("-----path-----")
