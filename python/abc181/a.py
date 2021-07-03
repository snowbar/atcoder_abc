from functools import reduce
from operator import add

v,t,s,d = map(int, input().split())

if t * v <= d and s * v >= d:
    print("No")
else:
    print("Yes")
#print(reduce(add, map(int, list(input())))