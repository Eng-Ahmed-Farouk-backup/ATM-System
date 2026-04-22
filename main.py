import sys
print("Welcome To ATM System")
usernames = ["ahmed"]
passwords = {"ahmed" : "test"}

    
def accounts() :
    ac = input("Enter the number of your choice : 1.Login 2.Signup 3.Exit ::: ")
    if ac == "3" :
        sys.exit()
    if ac == "1" :
        username1 = input("Enter your Username : ")
        if username1 in usernames :
            passw = input("Enter your Password : ")
            if passw == passwords[username1] :
                print("you Logged in !")
                main()
            else :
                print("Wrong Password Please Try again")
        else :
            print("Wrong Username please try again")
    if ac == "2" :
        username1 = "null" # store the intger with null cuz I can't return an empty Variable.
        auth = "null" #same as username1
        username2 = input("Please Enter a Username : ")
        usernames.append(username2)
        passwo = input("Please Enter a Password :::::  ")
        passwords[username2] = passwo
        print("account Created ! please Login.")
    return username1 , auth
