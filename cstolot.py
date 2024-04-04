def cstolot(str):
   lot = []
   for i in str.split(';'):
       lot.append(tuple(i.split('=')))
   return lot
 
cs="a=b;c=d;e=f;g=h"
print(cstolot(cs))

