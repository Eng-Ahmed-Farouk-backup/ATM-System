
print("Welcome To Bank System\n")
usernames = ["ahmed"]
passwords = {"ahmed" : "test"}
balances = {"ahmed" : 500}

def q () :
    ac = input("Enter the number of your choice : 1.Login 2.Signup 3.Exit ::: ")
    if ac in ["1","2","3"] :
        return ac
    else :
        print("please Enter a valid Choice")
        return q()

def accounts() :
    ac = q()
    if ac == "3" :
        sys.exit()
    elif ac == "1" :
        username1 = input("Enter your Username : ")
        if username1 in usernames :
            passw = input("Enter your Password : ")
            if passw == passwords[username1] :
                print("you Logged in !")
                return username1
            else :
                print("Wrong Password Please Try again")
                return accounts()
        else :
            print("Wrong Username please try again")
            return accounts()

    elif ac == "2" :
        username1 = input("Please Enter a Username : ")
        usernames.append(username1)
        passwo = input("Please Enter a Password :::::  ")
        passwords[username1] = passwo
        balances[username1] = 0
        print("account Created!")
        return username1

def main(username11) :
    choice = input("Please enter the Number of your Choice :\n 1.Withdraw \n 2.Deposit \n 3.Check balance \n 4.Transfer to other Bank Account \n ::::  ")
    
    if choice == "3" : 
        print("Hey",username11,"your balance is :::: ",balances[username11],"USD")

    elif choice == "2" :
        deposit = input("Please Enter the amount of money You want to Deposit : ")
        try :
            deposit = int(deposit)
            balances[username11] = deposit + balances[username11]
            print("You Deposited",deposit,"USD into your balance.")
        except :
            print("please write a valid Number to deposit")
            return

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

    elif choice == "4" :
        account_transfer(username11)

def account_transfer(giver) :
    taker = input("Please Enter the Reciever Bank Username : ")
    
    if taker in usernames and taker != giver :
        
        am = input("Please Enter the Amount you want to Transfer : ")
        try :
            am = int(am)
            if am <= balances[giver] :
                balances[giver] = balances[giver] - am
                balances[taker] = am + balances[taker]
            else :
                print("Please Enter a Valid Amount")
        except :
            print("please Enter a Valid Value")
    else :
        print("Please Enter a Valid Username")


while True :
    accc = accounts()
    if accc :
        main(accc)
