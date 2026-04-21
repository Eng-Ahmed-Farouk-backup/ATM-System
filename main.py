print("Welcome To ATM System")
usernames = ["ahmed"]
passwords = {"ahmed" : "test"}
auth = str
username1 = str
def accounts() :
    ac = input("Enter the number of your choice : 1.Login 2.Signup 2.Exit ::: ")
    if ac == "3" :
        while True :
            break
    if ac == "1" :
        username1 = input("Enter your Username : ")
        if username1 in usernames :
            passw = input("Enter your Password : ")
            if passw == passwords[username1] :
                auth = "true"
            else :
                print("Wrong Password Please Try again")
        else :
            print("Wrong Username please try again")
    return username1 , auth
