a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0
def sum(i,j,k):
    return i * 500 + j * 100 + k * 50

for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if sum(i,j,k) > x:
                break
            if sum(i,j,k) == x:
                count += 1
                break
print(count)