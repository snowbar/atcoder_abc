a, b = map(int, input().split())

def isOdd(num):
    return (num % 2 == 1)

def main():
    mul = a * b
    if isOdd(mul):
        print("Odd")
    else:
        print("Even")
        
main()