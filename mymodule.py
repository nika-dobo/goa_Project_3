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