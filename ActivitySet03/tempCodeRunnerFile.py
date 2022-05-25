def gcd(a,b):
    if a<b:
        t=b
        b=a
        a=t
    while b!=0:
        t=b
        b=a%b
        a=t
    print(a)