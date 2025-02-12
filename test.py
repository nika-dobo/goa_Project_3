import mymodule as my





while True:    
    mobile_number = input("Enter your mobile number: ")
    
    if len(mobile_number) == 9 and mobile_number.isdigit(): 
        print("Your mobile number is valid.")
        break
    else:
        print("Invalid mobile number. Please enter a 9-digit number.")