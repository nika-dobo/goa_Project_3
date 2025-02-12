import mymodule as my


Feedback = int(input("Give us Feedback (1-10): "))
if Feedback >= 7:
    print("Thank you, wish you best.")

elif Feedback >= 5 and Feedback <= 6:
    Answer = input(("What issues you complain about, give us Feedback: "))

elif Feedback >= 3 and Feedback <= 4:
    Answer2 = input(("Did our SupporTeam do something?, give us Feedback: "))

else:
    print("You can come to office and we can complain about it.")