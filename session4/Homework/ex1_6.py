sheep = [5, 7, 300, 90, 24, 50 ,75]
print("Hello, my name is Khai and these are my sheep sizes: ",sheep, sep = "\n" )
m = max(sheep)
print("Now my biggest sheep has size", m,"let's shear it")
ind = sheep.index(m)
sheep[ind] = 8
print("After shearing, here is my flock", sheep, sep = "\n")
for u in range(3):
    print("MONTH", u + 1, ":")
    for i in sheep:
        num = sheep.index(i)
        sheep[num] = i + 50
    print("One month has passed, now here is my flock", sheep, sep = "\n")
    if u !=2:
        m = max(sheep)
        print("Now my biggest sheep has size", m,"let's shear it")
        ind = sheep.index(m)
        sheep[ind] = 8
        print("After shearing, here is my flock", sheep, sep = "\n")
    else:
        s = 0
        for v in sheep:
            s = s + v
        print("My flock has size in total: ", s)
        print("I would get", s, "* 2$ =", s * 2, "$")
