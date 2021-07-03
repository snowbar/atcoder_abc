from functools import reduce
from operator import add

n = int(input())
a_list = sorted(list(map(int, input().split())), reverse=True)

alice_list = list()
bob_list = list()

for i in range(n):
    if i % 2 == 0:
        alice_list.append(a_list[i])
    else:
        bob_list.append(a_list[i])

print(reduce(add, alice_list) - reduce(add, bob_list))