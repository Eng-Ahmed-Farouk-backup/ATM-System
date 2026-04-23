import sys

print("Welcome To Bank System\n")
usernames = ["ahmed"]
passwords = {"ahmed" : "test"}
balances = {"ahmed" : 500}
history = {"ahmed" : []}
pins = {"ahmed" : "1234"}

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
                pin1 = input("Enter your PIN : ")
                if pin1 == pins[username1] :
                    print("you Logged in !")
                    return username1
                else :
                    print("Wrong PIN")
                    return accounts()
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
        pin2 = input("Please Enter a PIN :::::  ")

        passwords[username1] = passwo
        balances[username1] = 0
        history[username1] = []
        pins[username1] = pin2

        print("account Created!")
        return username1

def main(username11) :
    while True :
        choice = input("Please enter the Number of your Choice :\n 1.Withdraw \n 2.Deposit \n 3.Check balance \n 4.Transfer \n 5.Show History \n 6.Logout \n 7.Change Password \n 8.Delete Account \n ::::  ")
        
        if choice == "3" : 
            print("Hey",username11,"your balance is :::: ",balances[username11],"USD")

        elif choice == "2" :
            deposit = input("Please Enter the amount of money You want to Deposit : ")
            try :
                deposit = int(deposit)
                balances[username11] += deposit
                history[username11].append("Deposited " + str(deposit))
                print("Done")
            except :
                print("Error")

        elif choice == "1" :
            withdraw = input("Please Enter the amount of money You want to Withdraw : ")
            try :
                withdraw = int(withdraw)
                if withdraw <= balances[username11] :
                    balances[username11] -= withdraw
                    history[username11].append("Withdrew " + str(withdraw))
                    print("Done")
                else :
                    print("Invalid")
            except :
                print("Error")

        elif choice == "4" :
            account_transfer(username11)

        elif choice == "5" :
            print("Your History")
            for x in history[username11] :
                print(x)

        elif choice == "6" :
            print("Logged out")
            return

        elif choice == "7" :
            old = input("Enter old password : ")
            if old == passwords[username11] :
                newp = input("Enter new password : ")
                passwords[username11] = newp
                history[username11].append("Changed Password")
                print("Done")
            else :
                print("Wrong")

        elif choice == "8" :
            conf = input("Enter YES: ")
            if conf == "YES" :
                usernames.remove(username11)
                del passwords[username11]
                del balances[username11]
                del history[username11]
                del pins[username11]
                print("Deleted")
                return
            else :
                print("Cancelled")

def account_transfer(giver) :
    taker = input("Please Enter the Reciever Bank Username : ")
    if taker in usernames and taker != giver :
        am = input("Please Enter the Amount you want to Transfer : ")
        try :
            am = int(am)
            if am <= balances[giver] :
                balances[giver] -= am
                balances[taker] += am
                history[giver].append("Sent " + str(am) + " USD to " + taker)
                history[taker].append("Received " + str(am) + " USD from " + giver)
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
