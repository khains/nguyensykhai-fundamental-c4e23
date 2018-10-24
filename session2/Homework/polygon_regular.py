from turtle import *
fillcolor("red")
for i in range(3, 7):
    if i % 2 == 0:
        pencolor("red")
    else:
        pencolor("blue")
    x = i
    for u in range(x):
        forward(100)
        left(360/x)
mainloop()