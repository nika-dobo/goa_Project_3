import random
import math
import datetime as dt
import time

def load(text,sec):
    print(text)
    time.sleep(sec)

personal_info = {
    1: "name",
    2: "surename",
    3: "age",
    4: "formal_address"
}
def info_print():
    for num, info in personal_info.items():
        print(f"{num} - {info}")

bill = {
        1: "Electricity",
        2: "Gas",
        3: "Water",
        4: "Sewage",
        5: "Internet",
        6: "Television"      
    }
def bill_print():
    for num, bill_name in bill.items():
        print(f"{num} - {bill_name}")

bank_func = {
            1: "Deposit",
            2: "Withdraw",
            3: "Transfer",
            4: "Balance",
            5: "Deposit money on mobile",
            6: "Bill payment",
            7: "View transaction history",
            8: "Apply for loan",
            9: "Loan closing",
            10: "Update personal information",
            11: "trading to GEL - USD",#usd buy = 2.90, sell = 3
            12: "trading to USD - GEL",#usd buy = 2.90, sell = 3
            13: "trading to GEL - EUR",#eur buy = 3.40, sell = 3.60
            14: "trading to EUR - GEL",#eur buy = 3.40, sell = 3.60
            15: "bitcoin",
            16: "more option",
            17: "credit/DEBT",
            18: "ip adress",
            19: "",
            20: "Exit"
            }

def print_dict():  
    for num, name in bank_func.items():
        print(f"{num} - {name}")


kid_func = {
            1: "Deposit",
            2: "Withdraw",
            3: "Transfer",
            4: "Balance",
            5: "Deposit money on mobile",
            7: "View transaction history",
            8: "Update personal information",
            9: "more option",
            10: "Exit"
}
def print_dict2():  
    for num, name in kid_func.items():
        print(f"{num} - {name}")


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
    for num, option in more.items():
        print(f"{num} - {option}")


bit = {
    1:"Buy",
    2:"Sell",
    3:"Exit"
}
def bit_print():
    for num, op in bit.items():
        print(f"{num} - {op}")

def ip():
    num1 = random.randrange(1, 999)
    num2 = random.randrange(1, 999)
    num3 = random.randrange(1, 999)
    num4 = random.randrange(1, 999)
    print(num1,num2,num3,num4, sep=".")      

def not_robot():
    print("test: you are robot")
    while True:
        robot =  random.randrange(100000, 999999999) 
        print(robot)
        ask_robot = int(input("enter code: "))
        if robot == ask_robot:
            print("you are not robo_gabriel")
            break
        else:
            print("you are robo_gabriel") 
             