import mymodule as my


while True:
    Answer_to_consultation2 = {
            1: "Accounts and cards",
            2: "Loans and Credits",
            3: "Internet and Mobile Banking",
            4: "Other Questions"

    }

    for num, name in Answer_to_consultation2.items():
            print(f"{num} - {name}")
    Answer_to_consultation = int(input("Enter which question you want to get answered: "))

    if Answer_to_consultation == 1:
            
            # ანგარიშები და ბარათები
            print("Accounts and cards:")
            question = {
            # 1როგორ გავხსნა საბანკო ანგარიში?
            1: "How do I open a bank account?",
            # 2რა სახის ანგარიშები გაქვთ?
            2: "What types of accounts do you offer?",
            # 3როგორ მოვითხოვო სადებეტო ან საკრედიტო ბარათი?
            3: "How can I apply for a debit or credit card?",
            # 4რა საბუთებია საჭირო ანგარიშის ან ბარათის გასახსნელად?
            4: "What documents are required to open an account or get a card?",
            # 5როგორ გავაუქმო საბანკო ანგარიში ან ბარათი?
            5: "How can I close a bank account or cancel a card?",
            # 6რა ვადაში გაიცემა ბარათი?
            6: "How long does it take to issue a card?",
            # 7როგორ შევამოწმო ჩემი ბალანსი?
            7: "How can I check my balance?",
            # 8როგორ დავბლოკო/გავაუქმო დაკარგული ან მოპარული ბარათი?
            8: "How do I block or cancel a lost or stolen card?",
            # 9შესაძლებელია თუ არა ბარათის საზღვარგარეთ გამოყენება?
            9: "Can the card be used abroad?",
            # 10რა უნდა გავაკეთო, თუ ბარათი ბანკომატში ჩაიჭედა?
            10: "What should I do if my card gets stuck in an ATM?",
            # 11როგორ შევუკვეთო ახალი PIN-კოდი ბარათისთვის?
            11: "How can I request a new PIN code for my card?"}

            for num, name in question.items():
                    print(f"{num} - {name}")

            questions = int(input("Enter which question u want to get answered: "))

            if questions == 1:
                    print("\nHow do I open a bank account?")
                    print("\nFirst, register, then enter your LogIn, and once you're done, you will access your account as usual.")

            elif questions == 2:
                    print("\nWhat types of accounts do you offer?")
                    print("\nWe have: Visa, MasterCard, PlusCard, SchoolCard/StudentCard.")

            elif questions == 3:
                    print("\nHow can I apply for a debit or credit card?")
                    print("\nGo to bank and talk to consultant")

            elif questions == 4:
                    print("\nWhat documents are required to open an account or get a card?")
                    print("\nTo create a card, you must be 18 or older. \nIf you are a minor, parental or guardian consent is required.")

            elif questions == 5:
                    print("\nHow can I close a bank account or cancel a card?")
                    print("\nTo close an account: Open the mobile banking app, go to Settings → Account & Personal Information → Deactivate/Close. \nIf you want to block or cancel a card, select the card in the mobile banking app, then choose the Cancel or Block option, enter your personal details, and confirm.")

            elif questions == 6:
                    print("\nHow long does it take to issue a card?")
                    print("\nThe school and student card will be issued within 7 business days.\nwhile the payroll card will be issued within 14 business days.")

            elif questions == 7:
                    print("\nHow can I check my balance?")
                    print("\nOpen mobile bank...")

            elif questions == 8:
                    print("\nHow do I block or cancel a lost or stolen card?")
                    print("\nselect the card in the mobile banking app, then choose the Cancel or Block option, enter your personal details, and confirm. \nif you want to reorder card contact Support Team (which we dont have)")

            elif questions == 9:
                    print("\nCan the card be used abroad?")
                    print("Yes, you can use you'r card everywhere.")

            elif questions == 10:
                    print("\nWhat should I do if my card gets stuck in an ATM?")
                    print("\nYou just need to contact your provider or Support team in the our bank")

            elif questions == 11:
                    print("\nHow can I request a new PIN code for my card?")
                    print("\nYou just need your phone and ID card if you dont have any of those contact the Support team in the our bank and we will help you.")



    elif Answer_to_consultation == 2:

            # სესხები და კრედიტები
            print("Loans and Credits")
            question2 = {

            # 1: "რა პირობებია სესხის მისაღებად?",
            1: "What are the conditions for obtaining a loan?",
            # 2: "რა დოკუმენტებია საჭირო სესხის ასაღებად?",
            2: "What documents are required to take out a loan?",
            # 3: "რამდენია მინიმალური და მაქსიმალური საპროცენტო განაკვეთი?",
            3: "What is the minimum and maximum interest rate?",
            # 4: "რა ვადით შეგიძლიათ სესხის გაცემა?",
            4: "For what period can you issue a loan?",
            # 5: "მაქვს თუ არა უფლება ვადაზე ადრე დავფარო სესხი?",
            5: "Do I have the right to repay the loan early?",
            # 6: "რა ჯარიმებია დაგვიანებული გადახდის შემთხვევაში?",
            6: "What are the penalties for late payments?",
            # 7: "როგორ შევამოწმო ჩემი სესხის სტატუსი?",
            7: "How can I check the status of my loan?",
            # 8: "შესაძლებელია თუ არა სესხის რესტრუქტურიზაცია?",
            8: "Is it possible to restructure the loan?",
            # 9: "მაქვს თუ არა საკრედიტო ისტორიის გადამოწმების შესაძლებლობა?",
            9: "Can I check my credit history?",
            # 10: "როგორ მოვითხოვო იპოთეკური სესხი?",
            10: "How can I apply for a mortgage loan?",
            }

            for num, name in question2.items():
                    print(f"{num} - {name}")

            questions2 = int(input("Enter which question u want to get answered: "))

            if questions2 == 1:
                    print("\nWhat are the conditions for obtaining a loan?")
                    print("\nGo to bank, then order the loan in 'Loan Departament'. \nYou need ID and PayCheck history.")


            elif questions2 == 2:
                    print("\nWhat documents are required to take out a loan?")
                    print("\nYou need ID card, Paycheck history and birth document.")


            elif questions2 == 3:
                    print("\nWhat is the minimum and maximum interest rate?")
                    print("\nIt depends on how many loan you want but it grows 5 - 10%.")


            elif questions2 == 4:
                    print("\nFor what period can you issue a loan?")
                    print("\nWe can give you loan from 3 month to 5 year.")


            elif questions2 == 5:
                    print("\nDo I have the right to repay the loan early?")
                    print("\nDepends on how long you take the loan if you take 3-12 month period you dont have. \nElse if you have 13-60 month you can.")


            elif questions2 == 6:
                    print("\nWhat are the penalties for late payments?")
                    print("\nYou will got penalties: Paycheck + 5%, of loan.")


            elif questions2 == 7:
                    print("\nHow can I check the status of my loan?")
                    print("\nSimply LogIn in your mobile bank.")


            elif questions2 == 8:
                    print("\nIs it possible to restructure the loan?")
                    print("\nSure you can but that wont help you.")


            elif questions2 == 9:
                    print("\nCan I check my credit history?")
                    print("\nSimply LogIn in your mobile bank.")


            elif questions2 == 10:
                    print("\nHow can I apply for a mortgage loan?")
                    print("\nYes, you can but you need atleast 50000$ of house and 1000$ car.")



    elif Answer_to_consultation == 3:

            # ინტერნეტ და მობაილ ბანკინგი
            print("Internet and Mobile Banking")
            questions3 = {
            # 1როგორ გავააქტიურო ინტერნეტ ბანკინგი?
            1: "How do I activate internet banking?",
            # 2როგორ შევცვალო ჩემი პაროლი?
            2: "How can I change my password?",
            # 3როგორ დავბლოკო ან გავაუქმო ინტერნეტ ბანკინგის ანგარიში?
            3: "How do I block or cancel my internet banking account?",
            # 4შესაძლებელია თუ არა გადარიცხვების ონლაინ შესრულება?
            4: "Is it possible to make online transfers?",
            # 5რა ლიმიტებია ინტერნეტ ბანკინგით გადარიცხვებზე?
            5: "What are the transfer limits in internet banking?",
            # 6როგორ დავაკავშირო ბარათი Google Pay-ს ან Apple Pay-ს?
            6: "How can I link my card to Google Pay or Apple Pay?"
            }

            for num, name in questions3.items():
                    print(f"{num} - {name}")

            questions3 = int(input("Enter which question u want to get answered: "))

            if questions3 == 1:
                    print("\nHow do I activate internet banking?")
                    print("\nYou should come to bank departament in you'r area.")

            elif questions3 == 2:
                    print("\nHow can I change my password?")
                    print("\nIn you'r account: Setting --> private access, then simply verification of you'r identity you will able to change the password.")

            elif questions3 == 3:
                    print("\nHow do I block or cancel my internet banking account?")
                    print("\nIn you'r account: Setting --> private access, then simply verification of you'r identity you will able to deactivate or delete account.")


            elif questions3 == 4:
                    print("\nIs it possible to make online transfers?")
                    print("\nYes you can. \nGo to online bank --> then transfer money, and simply verification you can make transaction.")

            elif questions3 == 5:
                    print("\nWhat are the transfer limits in internet banking?")
                    print("\nThere is no limits, we are built differents.")

            elif questions3 == 6:
                    print("\nHow can I link my card to Google Pay or Apple Pay?")
                    print("\nJust add the card on your Google Pay or Apple Pay. We will handle next.")