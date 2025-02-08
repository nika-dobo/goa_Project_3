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
    balance = 0
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
            bank_function = {
            1: "Deposit",
            2: "Withdraw",
            3: "Transfer",
            4: "Balance",
            5: "Mobile recharge",
            6: "Bill payment",            
            7: "change password",
            8: "change email",
            9: "change mobile number",
            10: "change account name",
            11: "Close account",
            12: "Open new account",
            13: "View transaction history",
            14: "Apply for loan",
            15: "Update address",
            16: "Update personal information",
            17: "Update account information",
            18: "trading to GEL - USD",#usd buy = 2.90, sell = 3
            19: "trading to USD - GEL",#usd buy = 2.90, sell = 3
            20: "trading to GEL - EUR",#eur buy = 3.40, sell = 3.60
            21: "trading to EUR - GEL",#eur buy = 3.40, sell = 3.60
            22: "Exit"    
            }
            for num, name in bank_function.items():
                print(f"{num} - {name}")

            break  
        else:
            my.load("Checking your account...",8)
            print("login failed")
            print("try again")
            continue
       








