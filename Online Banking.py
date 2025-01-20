#Creating a list of user
#Username = ['John', 'Ryan', 'Oscar', 'Riley']
#Userpin = [3542, 5687, 9087, 8652]
#User_Balance = [20000, 10000, -15000, 30000]


#Creating Dictionary containing User Data
Bank_Data = {
    1001: {'Username': 'John', 'Userpin': 3542, 'User_Balance': 20000, 'Fullname': 'John Bush', 'Age': 20, 'Location': 'England', 'Occupation': 'Trader'},
    1002: {'Username': 'Ryan', 'Userpin': 5687, 'User_Balance': 10000, 'Fullname': 'Ryan Ayobami','Age': 19, 'Location': 'Nigeria', 'Occupation': 'Student'},
    1003: {'Username': 'Oscar', 'Userpin': 9087, 'User_Balance': -15000, 'Fullname': 'Oscar Scott', 'Age': 52, 'Location': 'Wales', 'Occupation': 'Unemployed'},
    1004: {'Username': 'Riley', 'Userpin': 8652, 'User_Balance': 30000, 'Fullname': 'Rilay Charles', 'Age': 41, 'Location': 'Ghana', 'Occupation': 'Self-Employed'}
}
#Welcome Page visible to User
print('Welcome to Strive Bank')
#Try Used to accept errors rather than break the code
try:

    #Assigning Variables to User Data
    Account_Input = int(input('Please enter your Account Number: '))
    Username_input = input('Please enter Username: ').capitalize()
    Userpin_input = int(input('Please enter your pin: '))

    #Loop for Logging into the User Account
    if Account_Input in Bank_Data:
        User_Data = Bank_Data[Account_Input]
        if Username_input == User_Data['Username'] and Userpin_input == User_Data['Userpin']:
            print('You have successfully login')
            
            #User trying to making decision while logged in
            Action_Count = 1
            Max_Count = 4
            #Loop for decision made by the User
            while Action_Count < Max_Count:
                print('Select 1 for Account Balance')
                print('Select 2 for User Profife')
                print('Select 3 for Withdrawal')
                print('Select 4 for Logout')
                Login_Option = int(input('Please enter your choice '))

                #Statement to check for User Account Balance
                if Login_Option == 1:
                    print(f'Your Account Balance is ${User_Data['User_Balance']}')
                
                #Statement to check for User Profile
                elif Login_Option == 2:
                    print(f'Fullname is {User_Data['Fullname']}')
                    print(f'Age is {User_Data['Age']}')
                    print(f'Current Location is {User_Data['Location']}')
                    print(f'Occupation is {User_Data['Occupation']}')
                
                #Withdrawal Statement
                elif Login_Option == 3:

                    #Loop to accept errors while withdrawing
                    while True:
                        try:
                            Amount = float(input('Kindly enter amount for Withdrawal '))
                            if User_Data['User_Balance'] >= Amount:
                                print(f'You have successfully withdrawel ${Amount}')
                                User_Data['User_Balance'] = User_Data['User_Balance'] - Amount
                                print(f'Your new Balance is ${User_Data['User_Balance']}')
                                break
                            else:
                                print('Insufficient Fund')
                        except ValueError:
                            print('Invalid amount please enter a valid number')

                #Logging out Statement
                elif Login_Option == 4:
                    print('Thanks for Visiting')
                    SystemExit()
                else:
                    print('Enter Valid Option')
            else:
                print('Try Again')

        elif Username_input == User_Data['Username'] and Userpin_input != User_Data['Username'] :
            print('Please re-enter valid User Pin')
        elif Username_input != User_Data['Username'] and Userpin_input == User_Data['Username'] :
            print('Please re-enter valid Username')
        else:
            print('Please re-enter valid Users Details')
    else:
        print('Enter Valid Account Number')
except ValueError:
    print('Account Number Must be Integer')