a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
d = b*b - 4*a*c
a_2 = a*2
if d<0:
    print("PT vo nghiem")
elif d == 0:
    x = (-b)/a_2
    print("PT co 1 nghiem:", x)
else:
    d_sprt = d**0.5
    x1 = (-b + d_sprt)/a_2
    x2 = (-b - d_sprt)/a_2
    print("PT co 2 nghiem:", x1, x2)