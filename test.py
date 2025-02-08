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

rara = int(input("enter: "))

if rara == 1:
    print("You chose", bank_function[1]) 