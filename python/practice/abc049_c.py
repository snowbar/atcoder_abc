a,b,c,d = "dream dreamer erase eraser"[::-1].split()
def isYes(s):
    while True:
        if len(s) == 7 and s == c:
            return True
        if len(s) == 6 and s == a:
            return True
        if len(s) == 5 and (s == b or s == d):
            return True

        if len(s) > 7 and s[:7] == c:
            s = s[7:]
        elif len(s) > 6 and s[:6] == a:
            s = s[6:]
        elif len(s) > 5 and (s[:5] == b or s[:5] == d):
            s = s[5:]
        else:
            return False
       
s = input()[::-1]
if isYes(s):
    print("YES")
else:
    print("NO")
