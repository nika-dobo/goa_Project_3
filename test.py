
from mymodule import bit_print as bit_p, bit


balance = 10000000  
btc_price = 96490  
btc_balance = 0.0  

while True:
    print("Balance:", balance, "USD <======> Bitcoin:", btc_balance, "BTC")
    bit_p()
    choice = input("what your chose: ")

    if choice == "1":  
        print("You chose", bit[1])
        amount = float(input("Enter amount to buy BTC: "))
        if amount <= balance:
            btc_balance += amount / btc_price
            balance -= amount
            print("You bought Bitcoin!")
        else:
            print("Not enough money!")

    elif choice == "2":  
        print("You chose", bit[1])
        amount_btc = float(input("Enter BTC amount to sell: "))
        if amount_btc <= btc_balance:
            balance += amount_btc * btc_price
            btc_balance -= amount_btc
            print("you sold Bitcoin!")
        else:
            print("not enough Bitcoin!")

    elif choice == "3":
        print("You chose", bit[1])  
        print("Goodbye!!!!!!!!!")
        break

    else:
        print("Invalid choice!!!!!!!!!!!!!")











