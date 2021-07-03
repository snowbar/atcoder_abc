from functools import reduce
from operator import add

def sum(num):
   return reduce(add, map(int, list(str(num))))

n, a, b = map(int, input().split())
total = 0

for i in range(1, n + 1):
    tmp = sum(i)
    if tmp >= a and tmp <= b:
        total += i

print(total)