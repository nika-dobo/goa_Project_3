# bank program

import mymodule as my
from mymodule import bank_func as bf, print_dict as pd, bill, bill_print as bp, more, more_print as mp, bit, bit_print as bit_p
import random
import math
import datetime as dt
import time


transaction_history = []


name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")
mobile_number = int(input("Enter your mobile number: "))    
ID = int(input("Enter your ID: "))
main_address = input("Enter your address(country/city/street): ")
formal_address = input("Enter your formal address(country/city/street): ")

gender = input("Enter your gender M/F: ")

if gender == "M" or gender == "Male" or gender == "male" or gender == "MALE":
    print("Male")
elif gender == "F" or gender == "Female" or gender == "FEMALE"  or gender == "female":
    print("Female")

print(" ")

if age >= 18:
    my.load("loading...",2)

    print(" ")


    password = input("Enter your password: ")
    acc_name = input("Enter your account name: ")
    balance = 1000
    btc_price = 96490  
    btc_balance = 0.0 
    my.load("loading...",2)


    print("your account created successfully")
    print("login to your account")
    password1= (input("Enter your password: "))
    acc_name1 = input("Enter your account name: ")
    email1 = input("Enter your email: ")
    mobile_number1 = int(input("Enter your mobile number: "))
    if password1 == password and acc_name1 == acc_name and email1 == email and mobile_number1 == mobile_number:
        my.load("Checking your account...",2)
        print("login successful")
        print(" ")
        while True:
            print(" ")
            pd()
            print("What will you choose?")
            Choice = int(input("Answer: "))
            print(" ")
            if 1 == 1:            
                
                if Choice == 1:
                    print("You chose", bf[1])   
                    print("enter exit if you dont want this")
                    exit = input("enter answer: ")
                    while True: 
                        if exit == "exit":
                            break  
                        elif exit != "exit":                 
                            print("How much money do you want to deposit?")
                            money = int(input("Amount of money: "))
                            my.load("Wait..", 3)
                            if money > 1500:
                                print("The amount exceeded the limit.")
                                print("limit 1500 gel")                       
                            else:
                                balance += money
                                history = money
                                transaction_history.append(history)
                                print("Your balance has been replenished", money, "gel", sep=" - ")
                                print("your balance", balance, sep=" - ") 
                                print("Would you like to receive a receipt?")
                                Answer = input("what your answer: ")
                                my.load("wait..", 2)
                                if Answer == "yes":
                                    my.Receipt("You replenish the balance", money)  
                                break                        


                elif Choice == 2:
                    print("You chose", bf[2])
                    print("enter exit if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            print("How much money do you want to Withdraw?")
                            money = int(input("Amount of money: "))
                            my.load("Wait..", 3)
                            if money > balance:
                                print("You do not have sufficient funds in your balance.")
                                print("please try again")
                            elif money > 500:
                                print("you cent Withdraw")
                                print("limit 500 gel")
                            else:
                                balance -= money 
                                history = -money
                                transaction_history.append(history)
                                print("Your balance has been deducted", money, "gel", sep=" - ")
                                print("your balance", balance, sep=" - ")
                                print("Would you like to receive a receipt?")
                                Answer = input("what your answer: ")
                                my.load("wait..", 2)
                                if Answer == "yes":
                                    my.Receipt("You're out of balance", money) 
                                break


                elif Choice == 3:
                    print("You chose", bf[3])
                    print("enter exit if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            print("How much money do you want to transfer")
                            money = int(input("Amount of money: "))
                            my.load("Wait..", 3)
                            if money > balance:
                                print("You do not have sufficient funds in your balance.")
                                print("please try again")
                            elif money > 500:
                                print("you cent Withdraw")
                                print("limit 500 gel")
                            else:
                                balance -= money
                                history = -money
                                transaction_history.append(history)   
                                print("Your balance has been deducted", money, "gel", sep=" - ")
                                print("your balance", balance, sep=" - ")
                                print("Would you like to receive a receipt?")
                                Answer = input("what your answer: ")
                                my.load("wait..", 2)
                                if Answer == "yes":
                                    my.Receipt("You transferred", money) 
                                break 
                        

                elif Choice == 4:
                    print("You chose", bf[4])
                    print("enter exit if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":                        
                            print("your balance", balance, sep=" - ")
                            break


                elif Choice == 5:
                    print("You chose", bf[5])
                    print("enter exit if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            print("To whom phone number do you want to transfer money")
                            number = int(input("enter phone number: "))
                            money = int(input("Amount of money: "))
                            my.load("serch number", 3)
                            if number != 9:
                                print("Error. phone number not founded")
                                print("please try again")
                                if money > balance:
                                    print("You do not have sufficient funds in your balance.")
                                    print("please try again")
                                elif money > 50:
                                    print("you cent Deposit")
                                    print("limit 50 gel")
                                else:
                                    balance -= money 
                                    history = -money
                                    transaction_history.append(history)  
                                    print("Your balance has been deducted", money, "gel", sep=" - ")
                                    print("your balance", balance, sep=" - ")
                                    print("Would you like to receive a receipt?")
                                    Answer = input("what your answer: ")
                                    my.load("wait..", 2)
                                    if Answer == "yes":
                                        my.Receipt("You transferred", money) 
                                    break  


                elif Choice == 6:
                    print("You chose", bf[6])
                    my.bill()
                    print("enter 'exit' if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            bill_choice = int(input("enter your bill choice: "))
                            print("enter 'exit' if you dont want this")
                            exit = input("enter answer: ")
                            if bill_choice == 1:
                                if exit == "exit":
                                    break  
                                elif exit != "exit":
                                    print("you chose", bill[1])
                                    num = random.randrange(0, 200)
                                    print("You need to pay the utilities:", num)
                                    print("do you want pay")
                                    Answer = input("enter your answer: ")
                                    if Answer == "yes":
                                        print("your balance", balance, sep=" - ")
                                        if num > balance:
                                            print("you cent pay \nyou dont have money")
                                            break
                                        else:
                                            print("You need to pay the utilities:", num)
                                            print("do you want pay")
                                            Answer = input("enter your answer: ")
                                            if Answer == "yes":
                                                print("You have been charged:", num) 
                                                balance -= num
                                                history = -num
                                                transaction_history.append(history)
                                                break
                                            elif Answer == "no":
                                                print("The operation was canceled")
                                                break
                                    elif Answer == "no":
                                        print("The operation was canceled")
                                        break

                            elif bill_choice == 2:
                                if exit == "exit":
                                    break  
                                elif exit != "exit":
                                    print("you chose", bill[2])
                                    num = random.randrange(0, 250)
                                    print("You need to pay the utilities:", num)
                                    print("do you want pay")
                                    Answer = input("enter your answer: ")
                                    if Answer == "yes":
                                        print("your balance", balance, sep=" - ")
                                        if num > balance:
                                            print("you cent pay \nyou dont have money")
                                            break
                                        else:
                                            print("You need to pay the utilities:", num)
                                            print("do you want pay")
                                            Answer = input("enter your answer: ")
                                            if Answer == "yes":
                                                print("You have been charged:", num) 
                                                balance -= num
                                                history = -num
                                                transaction_history.append(history)
                                                break
                                            elif Answer == "no":
                                                print("The operation was canceled")
                                                break
                                    elif Answer == "no":
                                        print("The operation was canceled")
                                        break

                            elif bill_choice == 3:
                                if exit == "exit":
                                    break  
                                elif exit != "exit":
                                    print("you chose", bill[3])
                                    num = random.randrange(0, 150)
                                    print("You need to pay the utilities:", num)
                                    print("do you want pay")
                                    Answer = input("enter your answer: ")
                                    if Answer == "yes":
                                        print("your balance", balance, sep=" - ")
                                        if num > balance:
                                            print("you cent pay \nyou dont have money")
                                            break
                                        else:
                                            print("You need to pay the utilities:", num)
                                            print("do you want pay")
                                            Answer = input("enter your answer: ")
                                            if Answer == "yes":
                                                print("You have been charged:", num) 
                                                balance -= num
                                                history = -num
                                                transaction_history.append(history)
                                                break
                                            elif Answer == "no":
                                                print("The operation was canceled")
                                                break
                                    elif Answer == "no":
                                        print("The operation was canceled")
                                        break    
                                
                            elif bill_choice == 4:
                                if exit == "exit":
                                    break  
                                elif exit != "exit":
                                    print("you chose", bill[4])
                                    num = random.randrange(0, 75)
                                    print("You need to pay the utilities:", num)
                                    print("do you want pay")
                                    Answer = input("enter your answer: ")
                                    if Answer == "yes":
                                        print("your balance", balance, sep=" - ")
                                        if num > balance:
                                            print("you cent pay \nyou dont have money")
                                            break
                                        else:
                                            print("You need to pay the utilities:", num)
                                            print("do you want pay")
                                            Answer = input("enter your answer: ")
                                            if Answer == "yes":
                                                print("You have been charged:", num) 
                                                balance -= num
                                                history = -num
                                                transaction_history.append(history)
                                                break
                                            elif Answer == "no":
                                                print("The operation was canceled")
                                                break
                                    elif Answer == "no":
                                        print("The operation was canceled")
                                        break

                            elif bill_choice == 5:
                                if exit == "exit":
                                    break  
                                elif exit != "exit":
                                    print("you chose", bill[5])
                                    num = random.randrange(0, 300)
                                    print("You need to pay the utilities:", num)
                                    print("do you want pay")
                                    Answer = input("enter your answer: ")
                                    if Answer == "yes":
                                        print("your balance", balance, sep=" - ")
                                        if num > balance:
                                            print("you cent pay \nyou dont have money")
                                            break
                                        else:
                                            print("You need to pay the utilities:", num)
                                            print("do you want pay")
                                            Answer = input("enter your answer: ")
                                            if Answer == "yes":
                                                print("You have been charged:", num) 
                                                balance -= num
                                                history = -num
                                                transaction_history.append(history)
                                                break
                                            elif Answer == "no":
                                                print("The operation was canceled")
                                                break
                                    elif Answer == "no":
                                        print("The operation was canceled")
                                        break

                            elif bill_choice == 6:
                                if exit == "exit":
                                    break  
                                elif exit != "exit":
                                    print("you chose", bill[6])
                                    num = random.randrange(0, 100)
                                    print("You need to pay the utilities:", num)
                                    print("do you want pay")
                                    Answer = input("enter your answer: ")
                                    if Answer == "yes":
                                        print("your balance", balance, sep=" - ")
                                        if num > balance:
                                            print("you cent pay \nyou dont have money")
                                            break
                                        else:
                                            print("You need to pay the utilities:", num)
                                            print("do you want pay")
                                            Answer = input("enter your answer: ")
                                            if Answer == "yes":
                                                print("You have been charged:", num) 
                                                balance -= num
                                                history = -num
                                                transaction_history.append(history)
                                                break
                                            elif Answer == "no":
                                                print("The operation was canceled")
                                                break
                                    elif Answer == "no":
                                        print("The operation was canceled")
                                        break

                            else:
                                print("error")
                                break


                elif Choice == 7:
                    print("You chose", bf[7])
                    print("enter 'exit' if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            print(transaction_history)
                            break


                elif Choice == 16:
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
                    

                

                
                elif Choice == 17:
                    while True:
                        mp()
                        cn = int(input("Soo, what do you want, Amigo?: "))
                        if cn == 1:
                            print("you chose", more[1])
                            old_password = input("Enter your current password to change email: ")
                            if old_password == password:
                                email = input("Enter new email: ")
                                print("Email successfully changed!")
                            else:
                                print("Incorrect password! Email not changed.")
                        elif cn == 2:
                            print("you chose", more[2])
                            password = input("Enter new password: ")
                        elif cn == 3:
                            print("you chose", more[3])
                            name == input("Enter new name: ")
                        elif cn == 4:
                            print("you chose", more[4])
                            print("Current email:", email)
                        elif cn == 5:
                            print("you chose", more[5])
                            print("Current password:", password)
                        elif cn == 6:
                            print("you chose", more[5])
                            print("End...")
                            break
                        else:
                            print("Error! Try again, my AMIGO!.")
            
                

    else:
        my.load("Checking your account...",8)
        print("login failed")
        print("something incorect")
        print("try again")

else:
    print("You are not allowed to open a bank account.")
    print("register kid account")
    my.load("loading...",2)

    mother_name = input("Enter your mother's name: ")
    mother_surname = input("Enter your mother's surname: ")
    mother_age = int(input("Enter your mother's age: "))

    print(" ")

    father_name = input("Enter your father's name: ")
    father_surname = input("Enter your father's surname: ")
    father_age = int(input("Enter your father's age: "))

    print(" ")






