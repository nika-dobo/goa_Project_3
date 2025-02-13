acc_name = "t"
print("The bank's managers are: Boss-Nika Dobo:crown:")
print("Luka Keleptrishvili🐱‍🏍")
print("and the double dragon Tornike Khurtsia:dragon: + Nikoloz Khechikashvili:dragon:")

print("Who do you want to contact, " + acc_name + "?")

while True:
    print("Boss Nika Dobo:crown: [1], Luka Keleptrishvili🐱‍🏍 [2], Tornike Khurtsia:dragon: [3], Nikoloz Khechikashvili:dragon: [4], Exit:x: [5];")
    
    ch = input("Who do you want to contact, " + acc_name + "?: ")
    
    if ch == "1":
        print("Discord => nikadobo, Phone => +995 599 12 ** ***")
    elif ch == "2":
        print("Discord => GallopinGoof, Phone => +995 577 45 ** ***")
    elif ch == "3":
        print("Discord => JUJI, Phone => +995 591 78 ** ***")
    elif ch == "4":
        print("Discord => Xechika, Phone => +995 555 33 ** ***")
    elif ch == "5":
        print("Okey........")
        break
    else:
        print("Wrong action!!!!!!")