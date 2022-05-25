import math
def in_put():
    n=int(input("Enter the number of rectangles"))
    return n 
#
def calc(n):
    for i in range(n):
        x1,y1,x2,y2,x3,y3=map(float, input("Enter number").split())
        area=math.fabs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
        print("Area of rectangle with vertices({},{}),({},{}) and ({},{}) is {}".format(x1,y1,x2,y2,x3,y3,area))
x=in_put()
calc(x)
