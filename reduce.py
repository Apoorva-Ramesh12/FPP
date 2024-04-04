num = [10,5,9,45,24]
from functools import reduce
maxi = reduce(lambda x,y:x if x>y else y,num)
print(maxi)

