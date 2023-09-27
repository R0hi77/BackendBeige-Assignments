optioins = {1: "check balance",
            3: "Buy airtime",
        2: "Send Money",
        }


initialBalance = 1000.00


def optionsMenu(menu):
    for value  in range(1,len(menu)+1):
        print(f"{value}: {menu[value]}")
    


def airtime (balance):
    amount = float(input("How airtime do you want to buy: "))
    if amount > balance:
        print("insufficient balance")
    else:
        print(f"You have successfully bought GHs{amount} airtime")
    balance = balance-amount/2
    return balance


def sendMoney(balance):
    receipeint = str(input("Enter receipeint number"))
    try:
        money = float(input("Enter amount you want to send :"))
        if money>balance:
            print("Insufficeint balance")   
        else:
            balance=balance-money
            print(f"You have successfully sent Ghc{money} to {receipeint}\nYour balance is GHc{balance}")
    except:
            pass
    return balance

while True :
    short_code = input("Enter shortcode :")
    if short_code == "*123#":
        optionsMenu(optioins)
        choice = int(input(": __"))
        if choice == 1:
            print(f"Your current balance is GHc{initialBalance}")
        elif choice == 2:
           initialBalance = sendMoney(initialBalance)
        elif choice ==3:
            initialBalance=airtime(initialBalance)
        else:
            choice = int(input("Invalid input. Try again"))
                
