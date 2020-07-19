#Función reduce
from functools import reduce

# l = range(1,10)
l = [2,3,5]
res = reduce(lambda a,b:2*a+b,l)
print(res)
