print("Welcome to Our Bank Services")
restart=("y")
chances =3
balance=10000
while chances>=0:
    pin=int(input("Enter Your Pin Code"))
    if pin ==(3045):
        print("Welcome Mr XYZ")
        while restart not in ("n","NO","no","No","N"):
            print("Please press 1 to show your balance\n")
            print("Please press 2 to make a Withdrawal \n")
            print("Please press 3 to Pay in\n")
            print("Please press 4 to Return Card \n")
            option =int(input("Enter Your Input"))
            if option==1:
                print("Your Account Balance is :",balance,"\n")
                restart=input("Would you Like to Go Back?")
                if restart in ("n","NO","no","No","N"):
                    print("Thank You")
                    break
            elif option==2:
                option2=("y","Y")
                withdrawal= float(input("How much would you like to withdraw?\n 100/500/2000"))
                if withdrawal in [100,500,2000]:
                    balance=balance-withdrawal
                    print("Your Balance is now :",balance,"\n")
                    restart = input("Would you Like to Go Back?")
                    if restart in ("n", "NO", "no", "No", "N"):
                        print("Thank You")
                        break
                elif withdrawal != [100,500,2000]:
                    print("Invalid Amount,Please Re-Try\n")
                    restart("y","Y")
                elif withdrawal==1:
                    withdrawal=float(input("Please Enter Desired Amount:"))
                elif option==3:
                    Pay_in=float(input("How much Amount do you want to Pay in?"))
                    balance=balance+Pay_in
                    print("Your Balance is now:",balance)
                    restart = input("Would you Like to Go Back?")
                    if restart in ("n", "NO", "no", "No", "N"):
                        print("Thank You")
                        break
                elif option==4:
                    print("Please Wait while your Card is Returned.\n")
                    print("Thank you for your Service")
                    break
                else:
                    print("Please Enter a correct Number\n")
                    restart=("y","Y")
    elif pin !=(3045):
        print("Incorrect Password !!\n")
        chances=chances-1
        print("You have just ",chances,"left")
        if chances==0:
            print("\n No more Trials\nPlease Contact your Bank to Further Details,Until then Your is Blocked\n")
            break

