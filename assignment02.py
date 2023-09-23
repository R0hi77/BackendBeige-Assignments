menu = {1: "check balance",
        2: "Send Money",
        3: "Buy airtime"
        }

initialBalance = 1000.00


def optionsMenu(dict):
    for value in range(1,len(menu)+1):
        print(f"{value}: {menu[Value]})


def airtime (balance):
    amount = float(input("How airtime do you want to buy: "))
    if amount > balance:
        print("insufficient balance")
    else:
        print(f"You have succesfully bought GHs{amount} airtime")
    balance = balance-amount/2
    return balance


def sendMoney(balance):
    receipeint = str(input("Enter receipeint number"))
    money = float(input("Enter amount you want to send :"))
    check=balance-money
    if check < 0:
        try:
            print(money)
        except:
            print("insufficient balance")
    else:
        balance=balance-money
        print(f"You have sucessfully sent Ghc{money} to {receipeint}\nYour balnce is GHc{balance}")
    return balance


while True :
    short_code = input("Enter short code :")
    if short_code == "*123#":
        optionsMenu(menu)
        choice = int(input(": __"))
        if choice == 1:
            print(f"Your current balance is GHc{initialBalance}")
        elif choice == 2:
           initialBalance = sendMoney(initialBalance)
        elif choice ==3:
            initialBalance=airtime(initialBalance)
        else:
            choice = int(input("Invalid input. Try again"))
                
