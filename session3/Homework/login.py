print("Hi there, this is a superuser gateway")
supuser = "c4e"
suppas = "codethechange"
user = input("Username: ")
if user == supuser:
    pas = input("Password: ")
    if pas == suppas:
        print("Welcome, ", user)
    else:
        print("Password is incorrect")
else:
    print("You are not superuser")