import random
import math
import datetime as dt
import time

def load(text,sec):
    print(text)
    time.sleep(sec)


def acc_info():
    name1 = input("Enter your name: ")
    surname1 = input("Enter your surname: ")
    age1 = int(input("Enter your age: "))
    ID1 = int(input("Enter your ID: "))
    card_ID1 = int(input("Enter your card ID: "))
    password1= (input("Enter your password: "))
    acc_name1 = input("Enter your account name: ")
    email1 = input("Enter your email: ")
    mobile_number1 = int(input("Enter your mobile number: ")) 
    main_address1 = input("Enter your address(country/city/street): ")
    formal_address1 = input("Enter your formal address(country/city/street): ")


def bank_function():
    bank_function = {
            1: "Deposit",
            2: "Withdraw",
            3: "Transfer",
            4: "Balance",
            5: "Deposit money on mobile",
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




def Receipt(info, money):
    print("--------you Receipt--------")
    print(dt.datetime.now())
    print("---------------------------")
    print(info)
    print(" ")
    print("-" + "your balance", money, "gel" + "-", sep=" - ")

