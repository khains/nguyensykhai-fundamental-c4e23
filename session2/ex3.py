from turtle import *
shape("turtle")
speed(0)
s= 10
for i in range(30):
    forward(s)
    left(90)
    s = s + 10 # s +=10
mainloop()