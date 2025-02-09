import random
import math
import datetime as dt
import time

def load(text,sec):
    print(text)
    time.sleep(sec)






bank_func = {
            1: "Deposit",
            2: "Withdraw",
            3: "Transfer",
            4: "Balance",
            5: "Deposit money on mobile",
            6: "Bill payment",
            7: "View transaction history",
            8: "Apply for loan",
            9: "Update address",
            10: "Update personal information",
            11: "Update account information",
            12: "trading to GEL - USD",#usd buy = 2.90, sell = 3
            13: "trading to USD - GEL",#usd buy = 2.90, sell = 3
            14: "trading to GEL - EUR",#eur buy = 3.40, sell = 3.60
            15: "trading to EUR - GEL",#eur buy = 3.40, sell = 3.60
            16: "bitcoin",
            17: "more option",
            18: "credit/DEBT",
            19: "Exit"    
            }

def print_dict():  
    for num, name in bank_func.items():
        print(f"{num} - {name}")


bill = {
        1: "Electricity",
        2: "Gas",
        3: "Water",
        4: "Sewage",
        5: "Internet",
        6: "Television"      
    }
def bill_print():
    for num1, bill_name in bill.items():
        print(f"{num1} - {bill_name}")


def Receipt(info, money):
    print("--------you Receipt--------")
    print(dt.datetime.now())
    print("---------------------------")
    print(info)
    print(" ")
    print("-" + "your balance", money, "gel" + "-", sep=" - ")



more = {
    1:"Change email",
    2:"Change password",
    3:"Change accaunt name",
    4:"See current email",
    5:"See current password",
    6:"End"
}
def more_print():
    for num2, option in more.items():
        print(f"{num2} - {option}")


bit = {
    1:"Buy",
    2:"Sell",
    3:"Exit"
}
def bit_print():
    for num3, op in bit.items():
        print(f"{num3} - {op}")

       