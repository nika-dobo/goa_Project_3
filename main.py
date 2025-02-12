# bank program

import mymodule as my
from mymodule import bank_func as bf, print_dict as pd, bill, bill_print as bp, more, more_print as mp, bit, bit_print as bit_p, personal_info as info, info_print as ip, kid_func as kd, print_dict2 as pd2
import random
import math
import datetime as dt
import time
import os
import csv

my.not_robot()

transaction_history = []

print( )

print(dt.datetime.now())

while True:
    name = input("\nEnter your name: ")
    surname = input("Enter your surname: ")
    if name == surname:
        print("name cent be surname too")
    else:
        break
age = int(input("Enter your age: "))
print("what do you have gmail/email")
answer = input("enter mail: ")
while True: 
    try:
        if answer == "gmail":
            gmail = input("enter your gmail: ")
            if gmail[-10] == "@":
                mail = gmail
                break
            else:
                print("gmail error")              
        elif answer == "email":
            email = input("enter your email: ")
            if email[-8] == "@":
                mail = email
                break
            else:
                print("email error")
        else:
            print("something incorect")
            break

    except IndexError:
        print("this is not mail!!")

while True:    
    mobile_number = input("Enter your mobile number: ")
    
    if len(mobile_number) == 9 and mobile_number.isdigit(): 
        print("Your mobile number is valid.")
        break
    else:
        print("Invalid mobile number. Please enter a 9-digit number.")
        


main_address = input("Enter your address(country/city/street): ")
formal_address = input("Enter your formal address(country/city/street): ")
while True:
    gender = input("Enter your gender M/F: ")

    if gender == "M" or gender == "Male" or gender == "male" or gender == "MALE" or gender == "m":
        print("Male")
        break
    elif gender == "F" or gender == "Female" or gender == "FEMALE"  or gender == "female" or gender == "f":
        print("Female")
        break
    else:
        print("gender not founded") 
        break   
    
while True:    
    password = input("Enter your password: ")
    
    if len(mobile_number) >= 8 and mobile_number.isdigit(): 
        print("Your password crieated")
        break
    else:
        print("Invalid pasword. Please enter a 8+ simbol.")


acc_name = input("Enter your account name: ")


print(" ")

if age >= 18:
    my.load("loading...",2)

    print(" ")

    balance = 10000
    usd_balance = 0
    eur_balance = 0
    btc_price = 96490  
    btc_balance = 0.0 
    loan = 0.0
    credit = 0.0
    
    my.load("loading...",2)


    print("your account created successfully")
    print("login to your account")
    acc_name1 = input("Enter your account name: ")
    email1 = input("Enter your email: ")
    mobile_number1 = input("Enter your mobile number: ")
    password1= input("Enter your password: ")
    while True:
        if password1 == password and acc_name1 == acc_name and email1 == mail and mobile_number1 == mobile_number:
            my.load("Checking your account...",2)
            print("login successful")
            print(" ")
            while True:
                print(" ")
                pd()
                print("\nWhat will you choose?")
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
                                    print("\nThe amount exceeded the limit.")
                                    print("limit 1500 gel")                       
                                else:
                                    balance += money
                                    history = money
                                    transaction_history.append(history)
                                    print("\nYour balance has been replenished", money, "gel", sep=" - ")
                                    print("your balance", balance, sep=" - ") 
                                    print("Would you like to receive a receipt?")
                                    Answer = input("what your answer: ")
                                    my.load("wait..", 2)
                                    if Answer == "yes":
                                        my.Receipt("You replenish the balance", money) 
                                        my.load("Wait..", 3) 
                                    break                        


                    elif Choice == 2:
                        print("\nYou chose", bf[2])
                        print("enter exit if you dont want this")
                        exit = input("enter answer: ")
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                print("\nHow much money do you want to Withdraw?")
                                money = int(input("Amount of money: "))
                                my.load("Wait..", 3)
                                if money > balance:
                                    print("\nYou do not have sufficient funds in your balance.")
                                    print("please try again")
                                elif money > 500:
                                    print("\nyou cent Withdraw")
                                    print("limit 500 gel")
                                else:
                                    balance -= money 
                                    history = -money
                                    transaction_history.append(history)
                                    print("\nYour balance has been deducted", money, "gel", sep=" - ")
                                    print("your balance", balance, sep=" - ")
                                    print("Would you like to receive a receipt?")
                                    Answer = input("what your answer: ")
                                    my.load("wait..", 2)
                                    if Answer == "yes":
                                        my.Receipt("You're out of balance", money)
                                        my.load("wait..", 4) 
                                    break


                    elif Choice == 3:
                        print("\nYou chose", bf[3])
                        print("enter exit if you dont want this")
                        exit = input("enter answer: ")
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                print("\nHow much money do you want to transfer")
                                money = int(input("Amount of money: "))
                                my.load("Wait..", 3)
                                if money > balance:
                                    print("\nYou do not have sufficient funds in your balance.")
                                    print("please try again")
                                elif money > 500:
                                    print("\nyou cent Withdraw")
                                    print("limit 500 gel")
                                else:
                                    balance -= money
                                    history = -money
                                    transaction_history.append(history)   
                                    print("\nYour balance has been deducted", money, "gel", sep=" - ")
                                    print("your balance", balance, sep=" - ")
                                    print("Would you like to receive a receipt?")
                                    Answer = input("what your answer: ")
                                    my.load("wait..", 2)
                                    if Answer == "yes":
                                        my.Receipt("You transferred", money) 
                                        my.load("wait..", 4)
                                    break 
                            

                    elif Choice == 4:
                        print("\nYou chose", bf[4])
                        print("enter exit if you dont want this")
                        exit = input("enter answer: ")
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":                        
                                print("\nyour balance", balance, sep=" - ")
                                my.load("wait..", 4)
                                break


                    elif Choice == 5:
                        print("\nYou chose", bf[5])
                        print("enter exit if you dont want this")
                        exit = input("enter answer: ")
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                print("\nTo whom phone number do you want to transfer money")
                                number = int(input("enter phone number: "))
                                len_number = len(number)
                                money = int(input("Amount of money: "))
                                my.load("serch number", 3)
                                if len_number != 9:
                                    print("\nError. phone number not founded")
                                    print("please try again")
                                    if money > balance:
                                        print("\nYou do not have sufficient funds in your balance.")
                                        print("please try again")
                                    elif money > 50:
                                        print("\nyou cent Deposit")
                                        print("limit 50 gel")
                                    else:
                                        balance -= money 
                                        history = -money
                                        transaction_history.append(history)  
                                        print("\nYour balance has been deducted", money, "gel", sep=" - ")
                                        print("your balance", balance, sep=" - ")
                                        print("Would you like to receive a receipt?")
                                        Answer = input("what your answer: ")
                                        my.load("wait..", 2)
                                        if Answer == "yes":
                                            my.Receipt("You transferred", money)
                                            my.load("wait..", 4) 
                                        break  


                    elif Choice == 6:
                        print("\nYou chose", bf[6])
                        bp()
                        print("\nenter 'exit' if you dont want this")
                        exit = input("enter answer: ")
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                bill_choice = int(input("enter your bill choice: "))
                                print("\nenter 'exit' if you dont want this")
                                exit = input("enter answer: ")
                                if bill_choice == 1:
                                    if exit == "exit":
                                        break  
                                    elif exit != "exit":
                                        print("\nyou chose", bill[1])
                                        num = random.randrange(0, 200)
                                        print("You need to pay the utilities:", num)
                                        print("do you want pay")
                                        Answer = input("enter your answer: ")
                                        if Answer == "yes":
                                            print("\nyour balance", balance, sep=" - ")
                                            if num > balance:
                                                print("\nyou cent pay \nyou dont have money")
                                                break
                                            else:
                                                print("\nYou need to pay the utilities:", num)
                                                print("do you want pay")
                                                Answer = input("enter your answer: ")
                                                if Answer == "yes":
                                                    print("\nYou have been charged:", num) 
                                                    balance -= num
                                                    history = -num
                                                    transaction_history.append(history)
                                                    break
                                                elif Answer == "no":
                                                    print("\nThe operation was canceled")
                                                    break
                                        elif Answer == "no":
                                            print("\nThe operation was canceled")
                                            break

                                elif bill_choice == 2:
                                    if exit == "exit":
                                        break  
                                    elif exit != "exit":
                                        print("\nyou chose", bill[2])
                                        num = random.randrange(0, 250)
                                        print("You need to pay the utilities:", num)
                                        print("do you want pay")
                                        Answer = input("enter your answer: ")
                                        if Answer == "yes":
                                            print("your balance", balance, sep=" - ")
                                            if num > balance:
                                                print("\nyou cent pay \nyou dont have money")
                                                break
                                            else:
                                                print("\nYou need to pay the utilities:", num)
                                                print("do you want pay")
                                                Answer = input("enter your answer: ")
                                                if Answer == "yes":
                                                    print("You have been charged:", num) 
                                                    balance -= num
                                                    history = -num
                                                    transaction_history.append(history)
                                                    break
                                                elif Answer == "no":
                                                    print("\nThe operation was canceled")
                                                    break
                                        elif Answer == "no":
                                            print("\nThe operation was canceled")
                                            break

                                elif bill_choice == 3:
                                    if exit == "exit":
                                        break  
                                    elif exit != "exit":
                                        print("\nyou chose", bill[3])
                                        num = random.randrange(0, 150)
                                        print("You need to pay the utilities:", num)
                                        print("do you want pay")
                                        Answer = input("enter your answer: ")
                                        if Answer == "yes":
                                            print("\nyour balance", balance, sep=" - ")
                                            if num > balance:
                                                print("\nyou cent pay \nyou dont have money")
                                                break
                                            else:
                                                print("\nYou need to pay the utilities:", num)
                                                print("do you want pay")
                                                Answer = input("enter your answer: ")
                                                if Answer == "yes":
                                                    print("\nYou have been charged:", num) 
                                                    balance -= num
                                                    history = -num
                                                    transaction_history.append(history)
                                                    break
                                                elif Answer == "no":
                                                    print("\nThe operation was canceled")
                                                    break
                                        elif Answer == "no":
                                            print("\nThe operation was canceled")
                                            break    
                                    
                                elif bill_choice == 4:
                                    if exit == "exit":
                                        break  
                                    elif exit != "exit":
                                        print("\nyou chose", bill[4])
                                        num = random.randrange(0, 75)
                                        print("\nYou need to pay the utilities:", num)
                                        print("do you want pay")
                                        Answer = input("enter your answer: ")
                                        if Answer == "yes":
                                            print("\nyour balance", balance, sep=" - ")
                                            if num > balance:
                                                print("\nyou cent pay \nyou dont have money")
                                                break
                                            else:
                                                print("\nYou need to pay the utilities:", num)
                                                print("do you want pay")
                                                Answer = input("enter your answer: ")
                                                if Answer == "yes":
                                                    print("You have been charged:", num) 
                                                    balance -= num
                                                    history = -num
                                                    transaction_history.append(history)
                                                    break
                                                elif Answer == "no":
                                                    print("\nThe operation was canceled")
                                                    break
                                        elif Answer == "no":
                                            print("\nThe operation was canceled")
                                            break

                                elif bill_choice == 5:
                                    if exit == "exit":
                                        break  
                                    elif exit != "exit":
                                        print("\nyou chose", bill[5])
                                        num = random.randrange(0, 300)
                                        print("You need to pay the utilities:", num)
                                        print("do you want pay")
                                        Answer = input("enter your answer: ")
                                        if Answer == "yes":
                                            print("\nyour balance", balance, sep=" - ")
                                            if num > balance:
                                                print("\nyou cent pay \nyou dont have money")
                                                break
                                            else:
                                                print("\nYou need to pay the utilities:", num)
                                                print("do you want pay")
                                                Answer = input("enter your answer: ")
                                                if Answer == "yes":
                                                    print("\nYou have been charged:", num) 
                                                    balance -= num
                                                    history = -num
                                                    transaction_history.append(history)
                                                    break
                                                elif Answer == "no":
                                                    print("\nThe operation was canceled")
                                                    break
                                        elif Answer == "no":
                                            print("\nThe operation was canceled")
                                            break

                                elif bill_choice == 6:
                                    if exit == "exit":
                                        break  
                                    elif exit != "exit":
                                        print("\nyou chose", bill[6])
                                        num = random.randrange(0, 100)
                                        print("You need to pay the utilities:", num)
                                        print("do you want pay")
                                        Answer = input("enter your answer: ")
                                        if Answer == "yes":
                                            print("\nyour balance", balance, sep=" - ")
                                            if num > balance:
                                                print("\nyou cent pay \nyou dont have money")
                                                break
                                            else:
                                                print("\nYou need to pay the utilities:", num)
                                                print("do you want pay")
                                                Answer = input("enter your answer: ")
                                                if Answer == "yes":
                                                    print("\nYou have been charged:", num) 
                                                    balance -= num
                                                    history = -num
                                                    transaction_history.append(history)
                                                    break
                                                elif Answer == "no":
                                                    print("\nThe operation was canceled")
                                                    break
                                        elif Answer == "no":
                                            print("\nThe operation was canceled")
                                            break

                                else:
                                    print("error")
                                    break


                    elif Choice == 7:
                        print("\nYou chose", bf[7])
                        print("enter 'exit' if you dont want this")
                        exit = input("enter answer: ")
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                print(transaction_history)
                                my.load("wait..", 4)
                                break

                    elif Choice == 8:
                        print("\nYou chose", bf[8])
                        print("enter 'exit' if you dont want this")
                        exit = input("enter answer: ")
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                job = input("have you job? ")
                                if job == "yes":
                                    print("you cen take loan")
                                    print("how mach money you take from job")
                                    money = int(input("Answer:" ))                                
                                    if money <= 2000 and money >= 500:
                                        print("you cen take 5000 gel")
                                        Answer = input("you want take loan.")
                                        print("loan Percentage is 25%")
                                        if Answer == "yes":
                                            print("Your balance has been replenished")
                                            balance += 5000
                                            loan += 5000
                                            break
                                        else:
                                            print("operation canceld") 
                                            break   
                                    elif money > 2000 and money <= 5000:
                                        print("you cen take 10000 gel")
                                        Answer = input("you want take loan.")
                                        print("loan Percentage is 25%")
                                        if Answer == "yes":
                                            print("Your balance has been replenished")
                                            balance += 10000
                                            loan += 10000
                                            break
                                        else:
                                            print("operation canceld") 
                                            break 
                                    elif money > 5000 and money <= 7500:
                                        print("you cen take 10000 gel")
                                        Answer = input("you want take loan.")
                                        print("loan Percentage is 25%")
                                        if Answer == "yes":
                                            print("Your balance has been replenished")
                                            balance += 15000
                                            loan += 15000
                                            break
                                        else:
                                            print("operation canceld") 
                                            break
                                    else:
                                        print("we dont give 15000gel more \n sorry") 
                                        break        
                                else:
                                    print("operation canceld")
                                    break


                    elif Choice == 9:
                        print("\nYou chose", bf[9])
                        print("enter 'exit' if you dont want this")
                        exit = input("enter answer: ")
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                print("your loan", loan, sep=" - ")
                                Answer == input("do you want close loan? ")
                                if Answer == "yes":
                                    if loan > balance:                                    
                                        my.load("Are you sure?", 3)
                                        print("sorry but you dont have money")
                                        break
                                    else:
                                        balance -= loan
                                        loan == 0
                                        print("your loan cloused")
                                        break    
                                else:
                                    print("operation canceld")  
                                    break      


                    elif Choice == 10:
                        print("\nYou chose", bf[10])
                        print("enter 'exit' if you dont want this")
                        exit = input("enter answer: ")
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                ip()
                                Answer = int(input("what you chose: "))
                                if Answer == 1:
                                    print("\nYou chose", info[1])
                                    name = input("chose your new name: ")
                                    print("name changed")
                                    break
                                elif Answer == 2:
                                    print("\nYou chose", info[2])
                                    surename = input("chose your new surename: ")
                                    print("surename changed")
                                    break                            
                                elif Answer == 3:
                                    while True:
                                        print("\nYou chose", info[3])
                                        age2 = input("chose your new age: ")
                                        if age < 18:
                                            print("you cent place 18")
                                            break                                  
                                        else:
                                            age == age2
                                            print("age changed")
                                            break
                                elif Answer == 4:
                                    print("\nYou chose", info[4])
                                    formal_address = input("chose your new formal address: ")
                                    print("formal address changed")
                                    break 
                                    

                    elif Choice == 11:
                        print("\nYou chose", bf[11])
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                print("How much USD do you want to buy for GEL?")
                                buy = int(input("answer: "))
                                buy1 = buy * 2.71
                                print("praice", buy1, sep=" - ")
                                if buy > balance:
                                    print("you cent buy \n you dont have money")
                                    break
                                else:
                                    print("Are you sure you want to buy?")
                                    answer = input("what you think: ")  
                                    if answer == "yes":
                                        balance -= buy1
                                        usd_balance += buy
                                        print("You bought", buy, sep=" - ")  
                                        break
                                    else:
                                        print("operation canceled")
                                        break    


                    elif Choice == 12:
                        print("\nYou chose", bf[12])
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                print("How much GEL do you want to buy for USD?")
                                buy = int(input("answer: "))
                                buy1 = buy * 0,36
                                print("praice", buy1, sep=" - ")
                                if buy > usd_balance:
                                    print("you cent buy \n you dont have money")
                                    break
                                else:
                                    print("Are you sure you want to buy?")
                                    answer = input("what you think: ")  
                                    if answer == "yes":
                                        usd_balance -= buy1
                                        balance += buy
                                        print("You bought", buy, sep=" - ")  
                                        break
                                    else:
                                        print("operation canceled")
                                        break                  


                    elif Choice == 13:
                        print("\nYou chose", bf[13])
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                print("How much EUR do you want to buy for GEL?")
                                buy = int(input("answer: "))
                                buy1 = buy * 2,90
                                print("praice", buy1, sep=" - ")
                                if buy > balance:
                                    print("you cent buy \n you dont have money")
                                    break
                                else:
                                    print("Are you sure you want to buy?")
                                    answer = input("what you think: ")  
                                    if answer == "yes":
                                        balance -= buy1
                                        eur_balance += buy
                                        print("You bought", buy, sep=" - ")  
                                        break
                                    else:
                                        print("operation canceled")
                                        break  


                    elif Choice == 14:
                        print("\nYou chose", bf[14])
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                print("How much GEL do you want to buy for EUR?")
                                buy = int(input("answer: "))
                                buy1 = buy * 0,36
                                print("praice", buy1, sep=" - ")
                                if buy > eur_balance:
                                    print("you cent buy \n you dont have money")
                                    break
                                else:
                                    print("Are you sure you want to buy?")
                                    answer = input("what you think: ")  
                                    if answer == "yes":
                                        eur_balance -= buy1
                                        balance += buy
                                        print("You bought", buy, sep=" - ")  
                                        break
                                    else:
                                        print("operation canceled")
                                        break  


                    elif Choice == 15:
                        print("\nYou chose", bf[15])
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                print("\nBalance:", balance, "USD <======> Bitcoin:", btc_balance, "BTC")
                                bit_p()
                                choice = input("what your chose: ")

                                if choice == "1":  
                                    print("\nYou chose", bit[1])
                                    amount = float(input("Enter amount to buy BTC: "))
                                    if btc_price <= balance:
                                        btc_balance += amount / btc_price
                                        balance -= amount
                                        print("\nYou bought Bitcoin!")
                                    else:
                                        print("\nNot enough money!")

                                elif choice == "2":  
                                    print("\nYou chose", bit[1])
                                    amount_btc = float(input("Enter BTC amount to sell: "))
                                    if amount_btc <= btc_balance:
                                        balance += amount_btc * btc_price
                                        btc_balance -= amount_btc
                                        print("\nyou sold Bitcoin!")
                                    else:
                                        print("\nnot enough Bitcoin!")

                                elif choice == "3":
                                    print("\nYou chose", bit[1])  
                                    print("Goodbye!!")
                                    break

                                else:
                                    print("\nInvalid choice!!")
                        
        
                    elif Choice == 16:
                        print("\nYou chose", bf[16])
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                mp()
                                cn = int(input("what do you want?: "))
                                if cn == 1:
                                    print("\nyou chose", more[1])
                                    old_password = input("Enter your current password to change email: ")
                                    if old_password == password:
                                        email = input("Enter new email: ")
                                        print("Email successfully changed!")
                                    else:
                                        print("\nIncorrect password! Email not changed.")
                                elif cn == 2:
                                    print("\nyou chose", more[2])
                                    password = input("Enter new password: ")
                                elif cn == 3:
                                    print("\nyou chose", more[3])
                                    name == input("Enter new name: ")
                                elif cn == 4:
                                    print("\nyou chose", more[4])
                                    print("Current email:", email)
                                elif cn == 5:
                                    print("\nyou chose", more[5])
                                    print("Current password:", password)
                                elif cn == 6:
                                    print("\nyou chose", more[5])
                                    print("End...")
                                    break
                                else:
                                    print("\nError! Try again")

                    elif Choice == 17:
                        print("\nYou chose", bf[17])
                        while True:
                            if exit == "exit":
                                break  
                            elif exit != "exit":
                                answer = input("Close/open credit: ")
                                if answer == "yes":
                                    num = input("how mach money do you want? ")
                                    credit += num
                                    break
                                else:
                                    if credit == 0:
                                        print("you dont have credit")
                                        break    
                                    else:
                                        if credit > balance:
                                            print("you dont have money")
                                            break
                                        else:
                                            print("you credit Closed")
                                            break


                    elif Choice == 18:
                        print("\nYou chose", bf[19])
                        my.ip()


                    elif Choice == 19:
                        print("\nYou chose", bf[19])
                        CARD_TYPES = ["Mastercard", "Visa", "American Express", "Discover", "UnionPay", "JCB", "Diners Club", "Maestro"]
                        CARD_CATEGORIES = ["Standard", "Premium", "Gold", "Platinum", "Business", "Corporate", "Student/School Card", "Travel Card", "Digital Card"]

                        CARD_BENEFITS = {
                            "Standard": "Basic banking services with no extra benefits.",
                            "Premium": "Includes cashback rewards and lower fees.",
                            "Gold": "Higher withdrawal limits and travel insurance.",
                            "Platinum": "Exclusive airport lounge access and concierge service.",
                            "Business": "Designed for business expenses with accounting tools.",
                            "Corporate": "For large companies with employee spending limits.",
                            "Student/School Card": "Lower fees, discounts on educational services.",
                            "Travel Card": "No foreign transaction fees, better exchange rates.",
                            "Digital Card": "Virtual card for online transactions with extra security."
                        }

                        def get_user_input(prompt):
                            while True:
                                value = input(prompt).strip()
                                if value:
                                    return value
                                print("❌ Error: The field cannot be empty!")

                        def get_numeric_input(prompt, min_val, max_val):
                            while True:
                                value = input(prompt).strip()
                                if value.isdigit() and min_val <= int(value) <= max_val:
                                    return int(value)
                                print(f"❌ Error: Please enter a number between {min_val} and {max_val}!")

                        def choose_option(options, title):
                            print(f"\n📌 Choose {title}:")
                            for i, option in enumerate(options, start=1):
                                print(f"{i}. {option}")

                            return options[get_numeric_input("👉 Enter the number: ", 1, len(options)) - 1]

                        def generate_card_number():
                            return "".join(str(random.randint(0, 9)) for _ in range(16))

                        def save_to_csv(data, filename="cards.csv"):
                            file_exists = os.path.isfile(filename)
                            with open(filename, mode="a", newline="", encoding="utf-8") as file:
                                writer = csv.writer(file)
                                if not file_exists:
                                    writer.writerow(["First Name", "Last Name", "Age", "Card Type", "Category", "Card Number", "Expiration", "Benefits"])
                                writer.writerow(data)

                        def main():
                            print("\n💳 Welcome to the Card Registration System! 💳\n")

                            first_name = get_user_input("👤 Enter your first name: ")
                            last_name = get_user_input("👤 Enter your last name: ")
                            age = get_numeric_input("🔢 Enter your age (10-100): ", 10, 100)

                            card_type = choose_option(CARD_TYPES, "Card Type")
                            card_category = choose_option(CARD_CATEGORIES, "Card Category")
                            
                            expiration_month = get_numeric_input("📆 Enter expiration month (1-12): ", 1, 12)
                            expiration_year = get_numeric_input("📆 Enter expiration year (2025-2035): ", 2025, 2035)
                            expiration_date = f"{str(expiration_month).zfill(2)}/{expiration_year}"

                            card_number = generate_card_number()

                            card_benefits = CARD_BENEFITS.get(card_category, "No additional benefits.")

                            save_to_csv([first_name, last_name, age, card_type, card_category, card_number, expiration_date, card_benefits])

                            print("\n✅ Card Successfully Created! ✅")
                            print("=" * 40)
                            print(f"👤 Cardholder: {first_name} {last_name} ({age} years old)")
                            print(f"💳 Card Type: {card_type}")
                            print(f"🏷️ Category: {card_category}")
                            print(f"🔢 Card Number: {card_number}")
                            print(f"📆 Expiration Date: {expiration_date}")
                            print(f"🎁 Benefits: {card_benefits}")
                            print("=" * 40)
                            print("\n📂 Data has been saved in cards.csv!")

                        if __name__ == "__main__":
                            main()
            

                    elif Choice == 20:
                        print("\nYou chose", bf[19])
                        Feedback = int(input("Give us Feedback (1-10): "))
                        if Feedback >= 7:
                            print("Thank you, wish you best.")

                        elif Feedback >= 5 or Feedback <= 6:
                            Answer = input(("What issues you complain about, give us Feedback: "))

                        elif Feedback >= 3 or Feedback <= 4:
                            Answer2 = input(("Did our SupporTeam do something?, give us Feedback: "))

                        elif Feedback >=1 or Feedback <=2:
                            print("You can come to office and we can complain about it.")

                        else:
                            print("enter 1-10")

                        while True:
                            answer = input("Are you sure? ")    
                            if answer == "no":
                                print("good :)")
                                break
                            elif answer == "yes":
                                answer = input("think agein: ") 
                                if answer == "no":
                                    print("good :)")
                                    break
                                elif answer == "yes": 
                                    print("no.\n buhahahaha")
                                    break


                    else:
                        print("your chous not founded")
                        break
                        

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




    kid_acc_name = input("Enter your account name: ")
    kid_email = input("Enter your email: ")
    kid_mobile_number = int(input("Enter your mobile number: "))
    kid_password= (input("Enter your password: "))
    if kid_password == password and kid_acc_name == acc_name and kid_email == mail and kid_mobile_number == mobile_number:
        balance = 100
        print(" ")
        while True:
            my.load("Checking your account...",2)
            print("login successful")
            print(" ")
            while True:
                print(" ")
                kd()
                print("\nWhat will you choose?")
                Choice = int(input("Answer: "))
                print(" ")
                if Choice == 1:
                    print("You chose", kd[1])   
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
                                print("\nThe amount exceeded the limit.")
                                print("limit 1500 gel")                       
                            else:
                                balance += money
                                history = money
                                transaction_history.append(history)
                                print("\nYour balance has been replenished", money, "gel", sep=" - ")
                                print("your balance", balance, sep=" - ") 
                                print("Would you like to receive a receipt?")
                                Answer = input("what your answer: ")
                                my.load("wait..", 2)
                                if Answer == "yes":
                                    my.Receipt("You replenish the balance", money) 
                                    my.load("Wait..", 3) 
                                break                        


                elif Choice == 2:
                    print("\nYou chose", kd[2])
                    print("enter exit if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            print("\nHow much money do you want to Withdraw?")
                            money = int(input("Amount of money: "))
                            my.load("Wait..", 3)
                            if money > balance:
                                print("\nYou do not have sufficient funds in your balance.")
                                print("please try again")
                            elif money > 500:
                                print("\nyou cent Withdraw")
                                print("limit 500 gel")
                            else:
                                balance -= money 
                                history = -money
                                transaction_history.append(history)
                                print("\nYour balance has been deducted", money, "gel", sep=" - ")
                                print("your balance", balance, sep=" - ")
                                print("Would you like to receive a receipt?")
                                Answer = input("what your answer: ")
                                my.load("wait..", 2)
                                if Answer == "yes":
                                    my.Receipt("You're out of balance", money)
                                    my.load("wait..", 4) 
                                break


                elif Choice == 3:
                    print("\nYou chose", kd[3])
                    print("enter exit if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            print("\nHow much money do you want to transfer")
                            money = int(input("Amount of money: "))
                            my.load("Wait..", 3)
                            if money > balance:
                                print("\nYou do not have sufficient funds in your balance.")
                                print("please try again")
                            elif money > 500:
                                print("\nyou cent Withdraw")
                                print("limit 500 gel")
                            else:
                                balance -= money
                                history = -money
                                transaction_history.append(history)   
                                print("\nYour balance has been deducted", money, "gel", sep=" - ")
                                print("your balance", balance, sep=" - ")
                                print("Would you like to receive a receipt?")
                                Answer = input("what your answer: ")
                                my.load("wait..", 2)
                                if Answer == "yes":
                                    my.Receipt("You transferred", money) 
                                    my.load("wait..", 4)
                                break
                

                elif Choice == 4:
                    print("\nYou chose", kd[4])
                    print("enter exit if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":                        
                            print("\nyour balance", balance, sep=" - ")
                            my.load("wait..", 4)
                            break


                elif Choice == 5:
                    print("\nYou chose", kd[5])
                    print("enter exit if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            print("\nTo whom phone number do you want to transfer money")
                            number = int(input("enter phone number: "))
                            len_number = len(number)
                            money = int(input("Amount of money: "))
                            my.load("serch number", 3)
                            if len_number != 9:
                                print("\nError. phone number not founded")
                                print("please try again")
                                if money > balance:
                                    print("\nYou do not have sufficient funds in your balance.")
                                    print("please try again")
                                elif money > 50:
                                    print("\nyou cent Deposit")
                                    print("limit 50 gel")
                                else:
                                    balance -= money 
                                    history = -money
                                    transaction_history.append(history)  
                                    print("\nYour balance has been deducted", money, "gel", sep=" - ")
                                    print("your balance", balance, sep=" - ")
                                    print("Would you like to receive a receipt?")
                                    Answer = input("what your answer: ")
                                    my.load("wait..", 2)
                                    if Answer == "yes":
                                        my.Receipt("You transferred", money)
                                        my.load("wait..", 4) 
                                    break


                elif Choice == 7:
                    print("\nYou chose", kd[7])
                    print("enter 'exit' if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            print(transaction_history)
                            my.load("wait..", 4)
                            break                    

            
                elif Choice == 8:
                    print("\nYou chose", kd[8])
                    print("enter 'exit' if you dont want this")
                    exit = input("enter answer: ")
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            ip()
                            Answer = int(input("what you chose: "))
                            if Answer == 1:
                                print("\nYou chose", info[1])
                                name = input("chose your new name: ")
                                print("name changed")
                                break
                            elif Answer == 2:
                                print("\nYou chose", info[2])
                                surename = input("chose your new surename: ")
                                print("surename changed")
                                break                            
                            elif Answer == 3:
                                while True:
                                    print("\nYou chose", info[3])
                                    age2 = input("chose your new age: ")
                                    if age > 18:
                                        print("you cent place 18")
                                        print("if you want got 18+ accaunt go to bank")
                                        break                                  
                                    else:
                                        age == age2
                                        print("age changed")
                                        break
                            elif Answer == 4:
                                print("\nYou chose", info[4])
                                formal_address = input("chose your new formal address: ")
                                print("formal address changed")
                                break


                elif Choice == 9:
                    print("\nYou chose", kd[9])
                    while True:
                        if exit == "exit":
                            break  
                        elif exit != "exit":
                            mp()
                            cn = int(input("what do you want?: "))
                            if cn == 1:
                                print("\nyou chose", more[1])
                                old_password = input("Enter your current password to change email: ")
                                if old_password == password:
                                    email = input("Enter new email: ")
                                    print("Email successfully changed!")
                                else:
                                    print("\nIncorrect password! Email not changed.")
                            elif cn == 2:
                                print("\nyou chose", more[2])
                                password = input("Enter new password: ")
                            elif cn == 3:
                                print("\nyou chose", more[3])
                                name == input("Enter new name: ")
                            elif cn == 4:
                                print("\nyou chose", more[4])
                                print("Current email:", email)
                            elif cn == 5:
                                print("\nyou chose", more[5])
                                print("Current password:", password)
                            elif cn == 6:
                                print("\nyou chose", more[5])
                                print("End...")
                                break
                            else:
                                print("\nError! Try again")


                elif Choice == 10:
                    print("\nYou chose", kd[10])
                    while True:
                        answer = input("Are you sure? ")    
                        if answer == "no":
                            print("good :)")
                            break
                        elif answer == "yes":
                            answer = input("think agein: ") 
                            if answer == "no":
                                print("good :)")
                                break
                            elif answer == "yes": 
                                print("no.\n buhahahaha")
                                break
                

                else:
                    print("your chous not founded")
                    break
