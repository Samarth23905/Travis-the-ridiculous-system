knownList = ['Samarth','Shreya','Praveen','Shwetha','Vishwas','Prateek','Shravya']
while True:
    print("Wlcome to the bank.")
    userName = input("Is there your account in this bank. If yes please enter your name: ").title()
    if userName in knownList:
        print("Wlcome back hope you wil have safe transactions {}.".format(userName))
        remove = input("Do you want to remove your account from this  bank. Type 'Yes' or 'No': ").lower()
        if remove == 'yes':
            knownList.remove(userName)
            print("You have successfully removed your account from the bank.")
            print(knownList)
        elif remove == 'no':
            print("You may proceed.")
            print(knownList)
        else:
            print("Invalid option.")
    else:
        print("Sorry you don't have account in this bank {}.".format(userName))
        addAcc = input("Do you want to create account in this bank 'Yes' or 'No': ").lower()
        if addAcc == 'yes':
            knownList += [userName]
            print(knownList)
        else:
            print("have a good day.")