import mymodule as my
from mymodule import print_shop as sh, bank_func as bf, print_elec as pe, print_item1 as pt1, print_item2 as pt2

blance = 0

while True:
    my.load("loading...", 3)
    print("\nYou chose", bf[22])
    sh()
    ans = int(input("\nwhat you chose: "))
    if ans == 1:
        print("\nYou chose", my.shop[1])
        pe()
        in_chose = int(input("enter you chose: "))
        if in_chose == 1:
            my.load("loading...", 2)
            print("\nYou chose", my.elec[1])
            print("\nwhat do you want buy?")
            pt1()
            answer = int(input("enter you chose: "))
            if answer == 1:
                my.load("loading...", 3)
                print("\nYou chose", my.elec_item[1])
                print("this item price 1500 gel")
                y_n = input("want buy yes/no ")
                if y_n == "yes":
                    if blance > 1500:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
                    
            elif answer == 2:
                print("\nYou chose", my.elec_item[2])
                print("this item price 2000 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 2000:
                        print("you buy this item")                        
                    else:
                        print("you dont have money")                      
                elif y_n == "no":
                    print("okey")                    
            elif answer == 3:
                print("\nYou chose", my.elec_item[3])
                print("this item price 1000 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 1000:
                        print("you buy this item")                     
                    else:
                        print("you dont have money")                      
                elif y_n == "no":
                    print("okey")                 
            else:
                print("this item dont fouded")    

        elif in_chose == 2:
            my.load("loading...", 3)
            print("\nYou chose", my.elec[2])
            print("\nwhat do you want buy?")
            pt2()
            answer = int(input("enter you chose: "))
            if answer == 1:
                print("\nYou chose", my.bracelets[1])
                print("this item price 500 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 500:
                        print("you buy this item")                       
                    else:
                        print("you dont have money")                        
                elif y_n == "no":
                    print("okey")
            elif answer == 2:
                print("\nYou chose", my.bracelets[2])
                print("this item price 700 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 700:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            elif answer == 3:
                print("\nYou chose", my.bracelets[3])
                print("this item price 450 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 450:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            else:
                print("this item dont fouded")

        elif in_chose == 3:
            my.load("loading...", 3)
            print("\nYou chose", my.elec[3])
            print("\nwhat do you want buy?")
            my.print_item3()
            answer = int(input("enter you chose: "))
            if answer == 1:
                print("\nYou chose", my.headphones[1])
                print("this item price 300 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 300:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            elif answer == 2:
                print("\nYou chose", my.headphoness[2])
                print("this item price 250 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 20:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            else:
                print("this item dont fouded")

        elif in_chose == 4:
            my.load("loading...", 3)
            print("\nYou chose", my.elec[4])
            print("\nwhat do you want buy?")
            my.print_item4()
            answer = int(input("enter you chose: "))
            if answer == 1:
                print("\nYou chose", my.keyboards[1])
                print("this item price 500 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 500:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            elif answer == 2:
                print("\nYou chose", my.keyboards[2])
                print("this item price 700 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 700:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            elif answer == 3:
                print("\nYou chose", my.keyboards[3])
                print("this item price 450 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 450:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            else:
                print("this item dont fouded")

        elif in_chose == 5:
            my.load("loading...", 3)
            print("\nYou chose", my.elec[5])
            print("\nwhat do you want buy?")
            my.print_item5()
            answer = int(input("enter you chose: "))
            if answer == 1:
                print("\nYou chose", my.mice[1])
                print("this item price 340 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 340:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            elif answer == 2:
                print("\nYou chose", my.mice[2])
                print("this item price 370 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 370:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            elif answer == 3:
                print("\nYou chose", my.mice[3])
                print("this item price 500 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 500:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            else:
                print("this item dont fouded")

        elif in_chose == 6:
            my.load("loading...", 3)
            print("\nYou chose", my.elec[6])
            print("\nwhat do you want buy?")
            my.print_item6()
            answer = int(input("enter you chose: "))
            if answer == 1:
                print("\nYou chose", my.power[1])
                print("this item price 150 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 150:
                        print("you buy this item")                        
                    else:
                        print("you dont have money")                       
                elif y_n == "no":
                    print("okey")
            elif answer == 2:
                print("\nYou chose", my.power[2])
                print("this item price 200 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 200:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            elif answer == 3:
                print("\nYou chose", my.power[3])
                print("this item price 175 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 175:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            else:
                print("this item dont fouded")

        elif in_chose == 7:
            my.load("loading...", 3)
            print("\nYou chose", my.elec[7])
            print("\nwhat do you want buy?")
            my.print_item7()
            answer = int(input("enter you chose: "))
            if answer == 1:
                print("\nYou chose", my.charging[1])
                print("this item price 100 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 100:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            elif answer == 2:
                print("\nYou chose", my.charging[2])
                print("this item price 75 gel")
                y_n = input("want buy yes/no")
                if y_n == "yes":
                    if blance > 75:
                        print("you buy this item")
                    else:
                        print("you dont have money")
                elif y_n == "no":
                    print("okey")
            else:
                print("this item dont fouded")    
        
    elif ans == 2:
        print("\nYou chose", my.shop[2])
        my.coupon()
        in_chose = int(input("enter you chose: "))
        if in_chose == 1:
            my.load("loading...", 2)
            print("\nYou chose", my.coupons[1])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 2:
            my.load("loading...", 2)
            print("\nYou chose", my.coupons[2])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 3:
            my.load("loading...", 2)
            print("\nYou chose", my.coupons[3])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 4:
            my.load("loading...", 2)
            print("\nYou chose", my.coupons[4])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 5:
            my.load("loading...", 2)
            print("\nYou chose", my.coupons[5])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 6:
            my.load("loading...", 2)
            print("\nYou chose", my.coupons[6])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 7:
            my.load("loading...", 2)
            print("\nYou chose", my.coupons[7])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        else:
            print("this coupons dont fouded")    

    elif ans == 3:
        print("\nYou chose", my.shop[3])
        my.gifts()
        in_chose = int(input("enter you chose: "))
        if in_chose == 1:
            my.load("loading...", 2)
            print("\nYou chose", my.gift[1])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 2:
            my.load("loading...", 2)
            print("\nYou chose", my.gift[2])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 3:
            my.load("loading...", 2)
            print("\nYou chose", my.gift[3])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 4:
            my.load("loading...", 2)
            print("\nYou chose", my.gift[4])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 5:
            my.load("loading...", 2)
            print("\nYou chose", my.gift[5])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 6:
            my.load("loading...", 2)
            print("\nYou chose", my.gift[6])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        else:
            print("this gift card dont fouded")

    elif ans == 4:
        print("\nYou chose", my.shop[4])
        my.Souvenir()
        in_chose = int(input("enter you chose: "))
        if in_chose == 1:
            my.load("loading...", 2)
            print("\nYou chose", my.Souvenir[1])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 2:
            my.load("loading...", 2)
            print("\nYou chose", my.Souvenir[2])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 3:
            my.load("loading...", 2)
            print("\nYou chose", my.Souvenir[3])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        else:
            print("this  dont fouded")    

    elif ans == 5:
        print("\nYou chose", my.shop[5])
        my.course()
        in_chose = int(input("enter you chose: "))
        if in_chose == 1:
            my.load("loading...", 2)
            print("\nYou chose", my.courses[1])
            print("this item price 250 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 250:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 2:
            my.load("loading...", 2)
            print("\nYou chose", my.courses[2])
            print("this item price 200 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 200:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 3:
            my.load("loading...", 2)
            print("\nYou chose", my.courses[3])
            print("this item price 250 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 4:
            my.load("loading...", 2)
            print("\nYou chose", my.courses[4])
            print("this item price 350 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 350:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        elif in_chose == 5:
            my.load("loading...", 2)
            print("\nYou chose", my.courses[5])
            print("this item price 150 gel")
            y_n = input("want buy yes/no")
            if y_n == "yes":
                if blance > 150:
                    print("you buy this coupon")
                else:
                    print("you dont have money")
            elif y_n == "no":
                print("okey")
        else:
            print("this  dont fouded")

    elif ans == 6:
        print("\nYou chose", my.shop[6])  
        break      