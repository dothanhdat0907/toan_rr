def gcd(a,b):
    if a > b:
        return gcd(b,a)
    if a == 0:
        return b
    if a % 2 == 0:
        if b % 2 == 0:
            return 2*gcd(a/2,b/2)
        else:
            return gcd(a/2,b)
    else:
        return gcd(a,b-a)        