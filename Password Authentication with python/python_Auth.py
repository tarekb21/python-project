# structure wrong re do 


import getpass


Accounts = {
    "Sally":"1234",
    "Jake":"3219",
    "Sean":"5362"
}

Username = input("please enter Username: \n")
Password = getpass.getpass("Enter password:")
for i in Accounts.keys():
    if Password == Accounts.values():
        print("login succesfful")
    else:
        Password = getpass.getpass("Enter password again:")
    