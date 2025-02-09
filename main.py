# bank program

import mymodule as my
import random
import math
import datetime as dt
import time



name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")
mobile_number = int(input("Enter your mobile number: "))    
ID = int(input("Enter your ID: "))
main_address = input("Enter your address(country/city/street): ")
formal_address = input("Enter your formal address(country/city/street): ")



print(" ")

if age < 18:
    print("You are not allowed to open a bank account.")
    print("register kid account")
    my.load("loading...",2)

    print(" ")

    mother_name = input("Enter your mother's name: ")
    mother_surname = input("Enter your mother's surname: ")
    mother_age = int(input("Enter your mother's age: "))

    print(" ")

    father_name = input("Enter your father's name: ")
    father_surname = input("Enter your father's surname: ")
    father_age = int(input("Enter your father's age: "))

    print(" ")

    card_ID = int(input("Enter your card ID: "))
    password = (input("Enter your password: "))
    acc_name = input("Enter your account name: ")
    balance = 1000
    my.load("loading...",2)

    print(" ")

    print("your account created successfully")
    
    print("login to your account")
    while True:
        my.acc_info()
        if my.card_ID1 == card_ID and my.password1 == password and my.acc_name1 == acc_name and my.ID1 == ID and my.name1 == name and my.surname1 == surname and my.age1 == age and my.email1 == email and my.mobile_number1 == mobile_number and my.main_address1 == main_address and my.formal_address1 == formal_address:
            my.load("Checking your account...",2)
            print("login successful")
            print(" ")

            my.bank_function()

            print("What will you choose?")
            Choice = int(input("Answer: "))

            if Choice == 1:
                print("You chose", my.bank_function[1])                
                while True:
                    print("How much money do you want to deposit?")
                    money = int(input("Amount of money: "))
                    my.load("Wait..", 3)
                    if money > 1500:
                        print("The amount exceeded the limit.")
                        print("limit 1500 gel")                       
                    else:
                        balance += money
                        print("Your balance has been replenished", money, "gel", sep=" - ")
                        print("your balance", balance, sep=" - ") 
                        print("Would you like to receive a receipt?")
                        Answer = input("what your answer: ")
                        my.load("wait..", 2)
                        if Answer == "yes":
                            my.Receipt("You replenish the balance", money)  
                        break                        

            elif Choice == 2:
                print("You chose", my.bank_function[2])
                while True:
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
                        print("Your balance has been deducted", money, "gel", sep=" - ")
                        print("your balance", balance, sep=" - ")
                        print("Would you like to receive a receipt?")
                        Answer = input("what your answer: ")
                        my.load("wait..", 2)
                        if Answer == "yes":
                            my.Receipt("You're out of balance", money) 
                        break

            elif Choice == 3:
                print("You chose", my.bank_function[3])
                while True:
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
                        print("Your balance has been deducted", money, "gel", sep=" - ")
                        print("your balance", balance, sep=" - ")
                        print("Would you like to receive a receipt?")
                        Answer = input("what your answer: ")
                        my.load("wait..", 2)
                        if Answer == "yes":
                            my.Receipt("You transferred", money) 
                        break 
                    
            elif Choice == 4:
                print("You chose", my.bank_function[4])
                print("your balance", balance, sep=" - ")

            elif Choice == 5:
                print("You chose", my.bank_function[5])
                while True:
                    print("To whom phone number do you want to transfer money")
                    number = int(input("enter phone number: "))
                    money = int(input("Amount of money: "))
                    my.load("serch number", 3)
                    if number != 9:
                        print("Error. phone number not founded")
                        print("please try again")
                    elif money > balance:
                        print("You do not have sufficient funds in your balance.")
                        print("please try again")
                    elif money > 50:
                        print("you cent Deposit")
                        print("limit 50 gel")
                    else:
                        balance -= money  
                        print("Your balance has been deducted", money, "gel", sep=" - ")
                        print("your balance", balance, sep=" - ")
                        print("Would you like to receive a receipt?")
                        Answer = input("what your answer: ")
                        my.load("wait..", 2)
                        if Answer == "yes":
                            my.Receipt("You transferred", money) 
                        break         
                            


            break 

        else:
            my.load("Checking your account...",8)
            print("login failed")
            print("something incorect")
            print("try again")
            break
       








