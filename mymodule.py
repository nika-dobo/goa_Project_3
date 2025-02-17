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
            11: "trading to GEL - USD",
            12: "trading to USD - GEL",
            13: "trading to GEL - EUR",
            14: "trading to EUR - GEL",
            25: "trading to RUB - GEL",
            26: "trading to GEL - RUB",
            15: "bitcoin",
            16: "more option",
            17: "credit/DEBT",
            18: "ip adress",
            19: "create card",
            20: "Consultation",
            21: "contacts",
            22: "shop",
            23: "auctions",
            24: "Exit"
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
    print("country: gerogia \nregion name: fasanauri \ncity: fasanauri \nISC: Magticom")     

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
             
shop = {
    1: "Electronics",
    2: "Discount coupons",
    3: "gift cards",
    4: "Souvenirs",
    5: "Training courses",
    6: "exit"
}      
def print_shop():  
    for num, name in shop.items():
        print(f"{num} - {name}")       

elec = {
    1:"Watch",
    2:"Fitness bracelets",
    3:"Wireless headphones",
    4:"Mechanical keyboards",
    5:"mice",
    6:"power banks",
    7:"Wireless charging",
    8:"Smart speakers"
}  
def print_elec():  
    for num, name in elec.items():
        print(f"{num} - {name}")      

elec_item = {
    1: "Apple Watch",
    2: "Samsung Galaxy Watch",
    3: "Xiaomi Mi Band"
} 
def print_item1():  
    for num, name in elec_item.items():
        print(f"{num} - {name}")   

bracelets = {
    1:'Xiaomi',
    2:'Huawei',
    3:'Fitbit'
} 
def print_item2():  
    for num, name in bracelets.items():
        print(f"{num} - {name}") 

headphones = {
    1:'AirPods',
    2:'Samsung Buds, Sony WF-1000XM5'
}   
def print_item3():  
    for num, name in headphones.items():
        print(f"{num} - {name}")       

keyboards = {
    1:'Razer',
    2:'Logitech',
    3:'Corsair'
}  
def print_item4():  
    for num, name in keyboards.items():
        print(f"{num} - {name}")   

mice = {
    1:'Logitech G Pro',
    2:'Razer DeathAdder',
    3:'SteelSeries'
}
def print_item5():  
    for num, name in mice.items():
        print(f"{num} - {name}")

charging = {
    1:'MagSafe',
    2:'Samsung Wireless Charger'
}
def print_item7():  
    for num, name in charging.items():
        print(f"{num} - {name}")

power ={
    1:'Anker',
    2:'Xiaomi',
    3:'Baseus'
}  
def print_item6():  
    for num, name in power.items():
        print(f"{num} - {name}")  

speakers = {
    1:'Google Nest',
    2:'Amazon Echo',
    3:'yandex'
} 
def print_item8():  
    for num, name in speakers.items():
        print(f"{num} - {name}")      

coupons = {
    1:"Streaming services",
    2:"Online courses",
    3:"Cloth",
    4:"Restaurants",
    5:"Cinemas",
    6:"Bowling",
    7:"billiards"
}
def coupon():  
    for num, name in coupons.items():
        print(f"{num} - {name}")


gift = {
    1:"Electronics",
    2:"Cloth",
    3:"Streaming services",
    4:"Trips",
    5:"Cinemas",
    6:"Restaurants",
    }
def gifts():  
    for num, name in gift.items():
        print(f"{num} - {name}")


Souvenirs = {
    1:"pens",
    2:"Diaries",
    3:"Flash drives",
}
def Souvenir():  
    for num, name in Souvenirs.items():
        print(f"{num} - {name}")

courses = {
    1:"Graphic design",
    2:"GOA",
    3:"cooking",
    4:"Unity",
    5:"Basics of financial literacy"
}
def course():  
    for num, name in courses.items():
        print(f"{num} - {name}")


auctions_func = {
    1: "Create auction",
    2: "Creative Authentic",
    3: "End auction",
    4: "Log out"
}
def print_auctions_func():  
    for num, name in auctions_func.items():
        print(f"{num} - {name}")

auctions = {}

def create_auction():
    print("auctions item:\n", auctions)
    item = input("enter item name: ")
    min_price = float(input("enter price: "))
    duration = int(input("Enter auction duration (in seconds): "))
    end_time = dt.datetime.now() + dt.timedelta(seconds=duration)
    
    auctions[item] = {
        "min_price": min_price,
        "current_price": min_price,
        "highest_bidder": None,
        "end_time": end_time
    }
    print(f"auctions '{item}' start! Minimum bid: {min_price} GEL. Will end in {end_time}.")

def place_bid():
    item = input("Enter the name of the product you want to bid on: ")
    if item not in auctions:
        print("There is no such auction!")
        return
    
    if dt.datetime.now() >= auctions[item]["end_time"]:
        print("The auction has already ended!")
        return
    
    bid = float(input("Enter your bid: "))
    if bid > auctions[item]["current_price"]:
        auctions[item]["current_price"] = bid
        auctions[item]["highest_bidder"] = input("Enter your name: ")
        print(f"Bid accepted! Current price {bid} GEL.")
    else:
        print("Your bid must be higher than the current price.!")

def end_auction():
    item = input("Enter the name of the completed auction: ")
    if item not in auctions:
        print("There is no such auction!")
        return
    
    if dt.datetime.now() < auctions[item]["end_time"]:
        print("The auction is not over yet!")
        return
    
    winner = auctions[item]["highest_bidder"]
    final_price = auctions[item]["current_price"]
    if winner:
        print(f"auctions '{item}' Completed! Winner: {winner} bet {final_price} GEL.")
    else:
        print(f"auctions '{item}' ended without a winner.")
    
    del auctions[item]


def pin():
    print("eter pin")
    while True:
        robot =  random.randrange(1000, 9999) 
        print(robot)
        ask_robot = int(input("enter code: "))
        if robot == ask_robot:
            print("corect pin")
            break
        else:
            print("uncorect pin") 