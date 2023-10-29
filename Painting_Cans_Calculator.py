






import math
h=int(input("Enter the height in meter: "))
w=int(input("Enter the width in meter: "))
coverage=int(input("Enter coverage by one can in square meter:- "))
def cans(Square,*numbers):
    area=numbers[0]*numbers[1]
    c=area/Square
    can=math.ceil(c)
    print(f"Number of cans: {can}")

cans(coverage,h,w)