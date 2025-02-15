import mymodule as my
from mymodule import bank_func as bf, print_dict as pd, bill, bill_print as bp, more, more_print as mp, bit, bit_print as bit_p, personal_info as info, info_print as ip, kid_func as kd, print_dict2 as pd2, print_shop as sh, print_elec as pe, print_item1 as pt1, print_item2 as pt2

Choice = int(input("enter num: "))

if Choice == 23:
    print("\nYou chose", bf[23])
    while True:
        print("\nauctions item:\n", my.auctions)
        my.print_auctions_func()
        choice = input("enter your chose: ")                                                            
        if choice == "1":
            print("you chose", my.auctions_func[1])
            my.create_auction()
        elif choice == "2":
            print("you chose", my.auctions_func[2])
            my.place_bid()
        elif choice == "3":
            print("you chose", my.auctions_func[3])
            my.end_auction()
        elif choice == "4":
            print("you chose", my.auctions_func[4])
            break
        else:
            print("error\n we dont founded this!")