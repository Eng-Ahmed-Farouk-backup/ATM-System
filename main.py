print("Welcome To ATM System")
usernames = ["ahmed"]
passwords = {"ahmed" : "test"}
balances = {"ahmed" : 500}
    
def accounts() :
    ac = input("Enter the number of your choice : 1.Login 2.Signup 3.Exit ::: ")
    if ac == "3" :
        print("fuck you")
    elif ac == "1" :
        username1 = input("Enter your Username : ")
        if username1 in usernames :
            passw = input("Enter your Password : ")
            if passw == passwords[username1] :
                print("you Logged in !")
                main(username1)
            else :
                print("Wrong Password Please Try again")
        else :
            print("Wrong Username please try again")
    elif ac == "2" :
        username1 = input("Please Enter a Username : ")
        usernames.append(username1)
        passwo = input("Please Enter a Password :::::  ")
        passwords[username1] = passwo
        balances[username1] = 0
        print("account Created!")
    return username1

def main(username11) :
    choice = input("Please enter the Number of your Choice :\n 1.Withdraw \n 2.Deposit \n 3.Check balance \n ::::  ")
    if choice == "3" : 
        print("Hey",username11,"your balance is :::: ",balances[username11],"USD")
    elif choice == "2" :
        deposit = input("Please Enter the amount of money You want to Deposit (I wish the ATM was that Easy) : ")
        if deposit == int :
            balances[username11] = deposit + balances[username11]
            print("You Deposited",deposit,"USD into your balance.")
        else :
            print("please write a valid Number to deposit")
    elif choice == "1" :
        withdraw = input("Please Enter the amount of money You want to Withdraw : ")
        try :
            withdraw = int(withdraw)
            if withdraw <= balances[username11] :
                balances[username11] = balances[username11] - withdraw
                print("You Withdrew",withdraw,"USD from your balance.")
            else : 
                print("Enter a Valid amount to withdraw")
        except :
            print("please Enter a Valid Vlaue")

while True :
    accc = accounts()
    main(accc)
