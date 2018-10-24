from random import randint

x = randint(0, 100)
print(x)
cloud = '''        .-~~~-.
  .- ~ ~-(       )_ _
 /                     ~ -.
|                           \
 \                         .'
   ~- . _____________ . -~
'''
if x<30:
    print("Rainy")
elif x<60:
    print(cloud)
else :
    print("Sunny")
