x = input("Password: ")
while True:
    if len(x) <= 8:
        print("mk phai dai hon 8")
    elif x.isalpha():
        print("mk phai co so")
    elif x.isupper() or x.islower() or x.isdigit():
        print("mk phai co chu hoa chu thuong")
    else:
        break
    x = input("Password: ")
   

