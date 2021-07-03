n, y = map(int, input().split())

def add(a, b, c):
    return a * 10000 + b * 5000 + c * 1000

def search():
    for a in range(n+1):
        for b in range(n - a + 1):
            sum = add(a, b, (n-a-b))
            if  sum == y:
                return "{} {} {}".format(a,b,n-a-b)
    return "-1 -1 -1"
            

def main():
    print(search())

main()