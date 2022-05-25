def gcd(a,b):
    if a<b:
        t=b
        b=a
        a=t
    while b!=0:
        t=b
        b=a%b
        a=t
    return float(a)

x=int(input("how many times?"))
for i in range(x):
    y=float(input("No of denominators"))
    lst=list(map(float,input("enter the denominators").split()))
    sx=0
    sy=1
    for j in lst:
        sx=sx*j+sy*1
        sy=sy*j
        g=gcd(sx,sy)
        sx=sx/g
        sy=sy/g
    for k in lst:
        j=1
        # print("{}/{}+".format(j,k),end="")
        print("%0.0f/%0.0f+"%(j,k),end="")
    # print("={}/{}".format(sx,sy),end="")
    print("=%0.0f/%0.0f"%(sx,sy),end="")


    