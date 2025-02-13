# bank program

import mymodule as my
from mymodule import bank_func as bf, print_dict as pd, bill, bill_print as bp, more, more_print as mp, bit, bit_print as bit_p, personal_info as info, info_print as ip, kid_func as kd, print_dict2 as pd2
import random
import math
import datetime as dt
import time
import os
import csv

def bank():

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
        my.load("loading...",5)

        print(" ")

        balance = 10000
        usd_balance = 0
        eur_balance = 0
        btc_price = 96490  
        btc_balance = 0.0 
        loan = 0.0
        credit = 0.0
        


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
                                            print("loan Percentage is 25% (6250)")
                                            if Answer == "yes":
                                                print("Your balance has been replenished")
                                                balance += 5000
                                                loan += 6250
                                                break
                                            else:
                                                print("operation canceld") 
                                                break   
                                        elif money > 2000 and money <= 5000:
                                            print("you cen take 10000 gel")
                                            Answer = input("you want take loan.")
                                            print("loan Percentage is 25% (12500)")
                                            if Answer == "yes":
                                                print("Your balance has been replenished")
                                                balance += 10000                            
                                                loan += 12500
                                                break
                                            else:
                                                print("operation canceld") 
                                                break 
                                        elif money > 5000:
                                            print("you cen take 10000 gel")
                                            Answer = input("you want take loan.")
                                            print("loan Percentage is 25% (18750)")
                                            if Answer == "yes":
                                                print("Your balance has been replenished")
                                                balance += 15000
                                                loan += 18750
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
                            print("\nYou chose", bf[18])
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
                            print("\nyou chose", bf[20])
                            while True:
                                Answer_to_consultation2 = {
                                        1: "Accounts and cards",
                                        2: "Loans and Credits",
                                        3: "Internet and Mobile Banking",
                                        4: "Other Questions"

                                }

                                for num, name in Answer_to_consultation2.items():
                                        print(f"{num} - {name}")
                                Answer_to_consultation = int(input("Enter which question you want to get answered: "))

                                if Answer_to_consultation == 1:
                                        
                                        # ანგარიშები და ბარათები
                                        print("Accounts and cards:")
                                        question = {
                                        # 1როგორ გავხსნა საბანკო ანგარიში?
                                        1: "How do I open a bank account?",
                                        # 2რა სახის ანგარიშები გაქვთ?
                                        2: "What types of accounts do you offer?",
                                        # 3როგორ მოვითხოვო სადებეტო ან საკრედიტო ბარათი?
                                        3: "How can I apply for a debit or credit card?",
                                        # 4რა საბუთებია საჭირო ანგარიშის ან ბარათის გასახსნელად?
                                        4: "What documents are required to open an account or get a card?",
                                        # 5როგორ გავაუქმო საბანკო ანგარიში ან ბარათი?
                                        5: "How can I close a bank account or cancel a card?",
                                        # 6რა ვადაში გაიცემა ბარათი?
                                        6: "How long does it take to issue a card?",
                                        # 7როგორ შევამოწმო ჩემი ბალანსი?
                                        7: "How can I check my balance?",
                                        # 8როგორ დავბლოკო/გავაუქმო დაკარგული ან მოპარული ბარათი?
                                        8: "How do I block or cancel a lost or stolen card?",
                                        # 9შესაძლებელია თუ არა ბარათის საზღვარგარეთ გამოყენება?
                                        9: "Can the card be used abroad?",
                                        # 10რა უნდა გავაკეთო, თუ ბარათი ბანკომატში ჩაიჭედა?
                                        10: "What should I do if my card gets stuck in an ATM?",
                                        # 11როგორ შევუკვეთო ახალი PIN-კოდი ბარათისთვის?
                                        11: "How can I request a new PIN code for my card?"}

                                        for num, name in question.items():
                                                print(f"{num} - {name}")

                                        questions = int(input("Enter which question u want to get answered: "))

                                        if questions == 1:
                                                print("\nHow do I open a bank account?")
                                                print("\nFirst, register, then enter your LogIn, and once you're done, you will access your account as usual.")

                                        elif questions == 2:
                                                print("\nWhat types of accounts do you offer?")
                                                print("\nWe have: Visa, MasterCard, PlusCard, SchoolCard/StudentCard.")

                                        elif questions == 3:
                                                print("\nHow can I apply for a debit or credit card?")
                                                print("\nGo to bank and talk to consultant")

                                        elif questions == 4:
                                                print("\nWhat documents are required to open an account or get a card?")
                                                print("\nTo create a card, you must be 18 or older. \nIf you are a minor, parental or guardian consent is required.")

                                        elif questions == 5:
                                                print("\nHow can I close a bank account or cancel a card?")
                                                print("\nTo close an account: Open the mobile banking app, go to Settings → Account & Personal Information → Deactivate/Close. \nIf you want to block or cancel a card, select the card in the mobile banking app, then choose the Cancel or Block option, enter your personal details, and confirm.")

                                        elif questions == 6:
                                                print("\nHow long does it take to issue a card?")
                                                print("\nThe school and student card will be issued within 7 business days.\nwhile the payroll card will be issued within 14 business days.")

                                        elif questions == 7:
                                                print("\nHow can I check my balance?")
                                                print("\nOpen mobile bank...")

                                        elif questions == 8:
                                                print("\nHow do I block or cancel a lost or stolen card?")
                                                print("\nselect the card in the mobile banking app, then choose the Cancel or Block option, enter your personal details, and confirm. \nif you want to reorder card contact Support Team (which we dont have)")

                                        elif questions == 9:
                                                print("\nCan the card be used abroad?")
                                                print("Yes, you can use you'r card everywhere.")

                                        elif questions == 10:
                                                print("\nWhat should I do if my card gets stuck in an ATM?")
                                                print("\nYou just need to contact your provider or Support team in the our bank")

                                        elif questions == 11:
                                                print("\nHow can I request a new PIN code for my card?")
                                                print("\nYou just need your phone and ID card if you dont have any of those contact the Support team in the our bank and we will help you.")



                                elif Answer_to_consultation == 2:

                                        # სესხები და კრედიტები
                                        print("Loans and Credits")
                                        question2 = {

                                        # 1: "რა პირობებია სესხის მისაღებად?",
                                        1: "What are the conditions for obtaining a loan?",
                                        # 2: "რა დოკუმენტებია საჭირო სესხის ასაღებად?",
                                        2: "What documents are required to take out a loan?",
                                        # 3: "რამდენია მინიმალური და მაქსიმალური საპროცენტო განაკვეთი?",
                                        3: "What is the minimum and maximum interest rate?",
                                        # 4: "რა ვადით შეგიძლიათ სესხის გაცემა?",
                                        4: "For what period can you issue a loan?",
                                        # 5: "მაქვს თუ არა უფლება ვადაზე ადრე დავფარო სესხი?",
                                        5: "Do I have the right to repay the loan early?",
                                        # 6: "რა ჯარიმებია დაგვიანებული გადახდის შემთხვევაში?",
                                        6: "What are the penalties for late payments?",
                                        # 7: "როგორ შევამოწმო ჩემი სესხის სტატუსი?",
                                        7: "How can I check the status of my loan?",
                                        # 8: "შესაძლებელია თუ არა სესხის რესტრუქტურიზაცია?",
                                        8: "Is it possible to restructure the loan?",
                                        # 9: "მაქვს თუ არა საკრედიტო ისტორიის გადამოწმების შესაძლებლობა?",
                                        9: "Can I check my credit history?",
                                        # 10: "როგორ მოვითხოვო იპოთეკური სესხი?",
                                        10: "How can I apply for a mortgage loan?",
                                        }

                                        for num, name in question2.items():
                                                print(f"{num} - {name}")

                                        questions2 = int(input("Enter which question u want to get answered: "))

                                        if questions2 == 1:
                                                print("\nWhat are the conditions for obtaining a loan?")
                                                print("\nGo to bank, then order the loan in 'Loan Departament'. \nYou need ID and PayCheck history.")


                                        elif questions2 == 2:
                                                print("\nWhat documents are required to take out a loan?")
                                                print("\nYou need ID card, Paycheck history and birth document.")


                                        elif questions2 == 3:
                                                print("\nWhat is the minimum and maximum interest rate?")
                                                print("\nIt depends on how many loan you want but it grows 5 - 10%.")


                                        elif questions2 == 4:
                                                print("\nFor what period can you issue a loan?")
                                                print("\nWe can give you loan from 3 month to 5 year.")


                                        elif questions2 == 5:
                                                print("\nDo I have the right to repay the loan early?")
                                                print("\nDepends on how long you take the loan if you take 3-12 month period you dont have. \nElse if you have 13-60 month you can.")


                                        elif questions2 == 6:
                                                print("\nWhat are the penalties for late payments?")
                                                print("\nYou will got penalties: Paycheck + 5%, of loan.")


                                        elif questions2 == 7:
                                                print("\nHow can I check the status of my loan?")
                                                print("\nSimply LogIn in your mobile bank.")


                                        elif questions2 == 8:
                                                print("\nIs it possible to restructure the loan?")
                                                print("\nSure you can but that wont help you.")


                                        elif questions2 == 9:
                                                print("\nCan I check my credit history?")
                                                print("\nSimply LogIn in your mobile bank.")


                                        elif questions2 == 10:
                                                print("\nHow can I apply for a mortgage loan?")
                                                print("\nYes, you can but you need atleast 50000$ of house and 1000$ car.")



                                elif Answer_to_consultation == 3:

                                        # ინტერნეტ და მობაილ ბანკინგი
                                        print("Internet and Mobile Banking")
                                        questions3 = {
                                        # 1როგორ გავააქტიურო ინტერნეტ ბანკინგი?
                                        1: "How do I activate internet banking?",
                                        # 2როგორ შევცვალო ჩემი პაროლი?
                                        2: "How can I change my password?",
                                        # 3როგორ დავბლოკო ან გავაუქმო ინტერნეტ ბანკინგის ანგარიში?
                                        3: "How do I block or cancel my internet banking account?",
                                        # 4შესაძლებელია თუ არა გადარიცხვების ონლაინ შესრულება?
                                        4: "Is it possible to make online transfers?",
                                        # 5რა ლიმიტებია ინტერნეტ ბანკინგით გადარიცხვებზე?
                                        5: "What are the transfer limits in internet banking?",
                                        # 6როგორ დავაკავშირო ბარათი Google Pay-ს ან Apple Pay-ს?
                                        6: "How can I link my card to Google Pay or Apple Pay?"
                                        }

                                        for num, name in questions3.items():
                                                print(f"{num} - {name}")

                                        questions3 = int(input("Enter which question u want to get answered: "))

                                        if questions3 == 1:
                                                print("\nHow do I activate internet banking?")
                                                print("\nYou should come to bank departament in you'r area.")

                                        elif questions3 == 2:
                                                print("\nHow can I change my password?")
                                                print("\nIn you'r account: Setting --> private access, then simply verification of you'r identity you will able to change the password.")

                                        elif questions3 == 3:
                                                print("\nHow do I block or cancel my internet banking account?")
                                                print("\nIn you'r account: Setting --> private access, then simply verification of you'r identity you will able to deactivate or delete account.")


                                        elif questions3 == 4:
                                                print("\nIs it possible to make online transfers?")
                                                print("\nYes you can. \nGo to online bank --> then transfer money, and simply verification you can make transaction.")

                                        elif questions3 == 5:
                                                print("\nWhat are the transfer limits in internet banking?")
                                                print("\nThere is no limits, we are built differents.")

                                        elif questions3 == 6:
                                                print("\nHow can I link my card to Google Pay or Apple Pay?")
                                                print("\nJust add the card on your Google Pay or Apple Pay. We will handle next.")
                            

                        elif Choice == 21:
                            print("\n you chose", bf[21]) 
                            print("The bank's managers are: Boss-Nika Dobo:crown:")
                            print("Luka Keleptrishvili🐱‍🏍")
                            print("and the double dragon Tornike Khurtsia:dragon: + Nikoloz Khechikashvili:dragon:")

                            print("Who do you want to contact, " + acc_name + "?")

                            while True:
                                print("Boss Nika Dobo:crown: [1], Luka Keleptrishvili🐱‍🏍 [2], Tornike Khurtsia:dragon: [3], Nikoloz Khechikashvili:dragon: [4], Exit:x: [5];")
                                
                                ch = input("Who do you want to contact, " + acc_name + "?: ")
                                
                                if ch == "1":
                                    print("Discord => nikadobo, Phone => +995 599 12 ** ***")
                                elif ch == "2":
                                    print("Discord => GallopinGoof, Phone => +995 577 45 ** ***")
                                elif ch == "3":
                                    print("Discord => JUJI, Phone => +995 591 78 ** ***")
                                elif ch == "4":
                                    print("Discord => Xechika, Phone => +995 579 28 20 07")
                                elif ch == "5":
                                    print("Okey........")
                                    break
                                else:
                                    print("Wrong action!!!!!!")   


                        elif Choice == 22:
                            print("\nYou chose", bf[22])
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
                break

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
