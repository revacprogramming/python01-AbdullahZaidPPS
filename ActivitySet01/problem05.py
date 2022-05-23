# Functions
def calcpay(h,r):
 if h>40:
    sly = 1.5*(h-40)*r+(40*r)
    print("The salary is {}".format(sly))
    return sly
 else:
    sly = h*r
    print("The salary is {}".format(sly))
    return sly

hours = float(input("enter hours \n"))
rate = float(input("enter hourly rate \n"))
gpay = calcpay(hours,rate)

