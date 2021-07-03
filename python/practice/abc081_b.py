def isOdd(num):
    return num % 2 == 1

def main():
    count = 0
    n = int(input())
    lists = list(map(int, input().split()))

    while True:
        for num in lists:
            if isOdd(num):
                return(count)
        lists = list(map(lambda n: n / 2, lists))
        count += 1

print(main())


