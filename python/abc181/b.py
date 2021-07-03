n, x = map(int, input().split())
a_list = list(map(int, input().split()))

a_list = list(filter(lambda y: y != x, a_list))
for i in range(len(a_list)):
    if i == len(a_list) - 1:
        print(a_list[i])
    else:
        print(a_list[i], end=" ")