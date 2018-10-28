print("Hi there, this is a superuser gateway")
supuser = "c4e"
suppas = "codethechange"
user = input("Username: ")
while user != supuser:
        print("You are not superuser")
        user = input("Username: ")
pas = input("Password: ")
while True:
    if pas != suppas:
        print("Password is incorrect")
        pas = input("Password: ")
    else:
        print("Welcome, ", user)
        break