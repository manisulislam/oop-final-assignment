class User:
    acc=0
    accounts={}
    total_balance=0
    loan_balance=0
    count_loan=0
    def __init__(self, name, email, address,type) -> None:
        User.acc+=1
        self.name= name
        self.email= email
        self.address= address
        self.type= type
        self.accNumber= User.acc
        self.current_balance=0
        self.transaction_history=[]
         
        # user= User(name, email, address,acc_type)
        # User.accounts[user.accNumber]=user
        
       
    
    
    # deposit functionality
    def deposit(self, amount):
        if amount>=0:
            self.current_balance+=amount
            User.total_balance+=amount
            self.transaction_history.append(f"congratulation...!!! {self.name} your {amount} deposited successfully..")
            print(f"{self.name} your deposit successfully ..!!!, your current balance is {self.current_balance} taka")
    
    # withdraw functionality
    def withdraw(self, amount):
        if User.total_balance==0:
            print(f"The bank is bankrupt.")
        elif amount<self.current_balance:
            self.current_balance-=amount
            self.transaction_history.append(f"congratulation...!!!{self.name} your {amount} amount withdraw successfully..")
            print(f"{self.name} your withdraw successfully...!!, your current balance is {self.current_balance} taka..")
        else:
            print(f"Withdrawal amount exceeded")
            
    
    # check balance functionality
    def check_available_balance(self):
        print(f"{self.name} your available balance is {self.current_balance} taka")
    
    
    # show transaction history
    def trsaction_history(self):
        for history in self.transaction_history:
            print(history)
    
    # loan functionality
    def loan(self, amount):
        # x=User.count_loan
        if Admin.status_loan==1:
            if User.count_loan<2:
                self.current_balance+=amount
                User.loan_balance+=amount
                User.count_loan+=1
                
                self.transaction_history.append(f"congratulation...!!!{self.name} your {amount} amount loan successfully..")
                print(f"{self.name} you take loan.. your current balance is {self.current_balance} taka..")
        
                
            else:
                print(f"{self.name} your can not loan more than two times..")
        else:
            print("Bank can not offer bank loan...")
    # transfer money functionality
    def transfer(self, recipient_account_number, amount):
        if recipient_account_number in User.accounts and recipient_account_number != self.accNumber:
            recipient = User.accounts[recipient_account_number]
            if amount > 0 and self.current_balance >= amount:
                self.current_balance -= amount
                recipient.current_balance += amount
                recipient.transaction_history.append(f"Received {amount} from {self.name}")
                self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
                print(f"{self.name}, you transferred {amount} taka to {recipient.name}. Your current balance is {self.current_balance} taka.")
            else:
                print("Insufficient balance for the transfer.")
        else:
            print("Recipient account does not exist or is invalid.")
class Admin:
    
    # loan status initially true
    status_loan=1
    # create account functionality
    def create_acc(self, name, email, address, acc_type):
        user= User(name, email, address,acc_type)
        User.accounts[user.accNumber]=user
        print(f"create an account successfully")
    
    # delete account functionality
    def delete_account(self, account_number):
        if account_number in User.accounts:
            del User.accounts[account_number]
            print(f"{account_number} deleted successfully")

        
    # see all list account
    def all_list_account(self):
        for account_number, user in User.accounts.items():
            print("---------------------------")
            print(f"Account number :", account_number)
            print(f"name : {user.name}")
            print(f"email : {user.email}")
            print(f"address : {user.address}")
            print(f"account type : {user.type}")
            print("------------------------")
       
    
    # check total available balance
    def total_balance(self):
        print(f"total loan balance is {User.total_balance}")
    # total loan amount
    def total_loan_amount(self):
        print(f"total loan balance is {User.loan_balance}")
    
    # loan on or of
    def loan_status(self, status):
        if status==1 or status==0:
            Admin.status_loan=status
        else:
            print("Invalid.. use (True or False)...")
        

while True:
    print("Choose your option as a admin or user :")
    print("1.Admin")
    print("2.User")
    print("3.Exit")
    
    op= int(input("press 1 or 2 or 3 :"))
    admin=Admin()
    if op==1:
        while True:
            
            print("choose your option from below :")
            print("1. create an new account ")
            print("2. delete an account")
            print("3. see all user list")
            print("4. check the total balance of the bank")
            print("5. check the total loan amount")
            print("6. on or off the loan feature of the bank")
            print("7. exit")
            
            choice = int(input("Enter your option :"))
            if choice==1:
                name=input("Enter your name :")
                email=input("Enter your email address :")
                address= input("Enter your address :")
                acc_type= input("Enter your account type savings or current :")
                admin.create_acc(name,email,address,acc_type)
            elif choice==2:
                delete_account_number= int(input("Enter your delete account number :"))
                admin.delete_account(delete_account_number)
            elif choice==3:
                admin.all_list_account()
            elif choice==4:
                admin.total_balance()
            elif choice==5:
                admin.total_loan_amount()
            elif choice==6:
                status= int(input("Enter your status True=1 or False=0 :"))
                admin.loan_status(status)
            elif choice==7:
                break
            else:
                print("Invalid choice :")
                break
    elif op==2:
        current_user=None
        while True:
            if current_user==None:
                print("......Currently no user....")
                print("Your option is below :")
                print("1. Create an account")
                print("2. Deposit ")
                print("3. Withdraw")
                print("4. Check available balance")
                print("5. Check transaction history")
                print("6. Take a loan")
                print("7. Transfer the amount")
                print("8. Exit")
            
                choice = int(input("Enter your choice :"))
                if choice==1:
                    name=input("Enter your name :")
                    email=input("Enter your email address :")
                    address= input("Enter your address :")
                    acc_type= input("Enter your account type (savings or current) :")
                    current_user=User(name,email, address,acc_type)
                    print(f"Congratulation..{name} your {acc_type} account created successfully..!!!")
                elif choice==2:
                    amount= int(input("Enter your amount for deposit :"))
                    current_user.deposit(amount)
                elif choice==3:
                    amount= int(input("Enter your amount for withdraw :"))
                    current_user.withdraw(amount)
                    
                elif choice==4:
                    current_user.check_available_balance()
                elif choice==5:
                    current_user.trsaction_history()
                    
                elif choice==6:
                    amount= int(input("Enter your amount for bank loan :"))
                    current_user.loan(amount)
                elif choice==7:
                    amount= int(input("Enter your amount for transfer:"))
                    current_user.transfer(amount)
                elif choice==8:
                    break
                else:
                    print("Invalid choice.. Please choose valid choice in the option..")
                    break
            else:
                print(f"......Currently user is {current_user.name}....")
                print("Your option is below :")
                print("1. Create an new account")
                print("2. Deposit ")
                print("3. Withdraw")
                print("4. Check available balance")
                print("5. Check transaction history")
                print("6. Take a loan")
                print("7. Transfer the amount")
                print("8. Exit")
            
                choice = int(input("Enter your choice :"))
                if choice==1:
                    name=input("Enter your name :")
                    email=input("Enter your email address :")
                    address= input("Enter your address :")
                    acc_type= input("Enter your account type (savings or current) :")
                    current_user=User(name,email, address,acc_type)
                    print(f"Congratulation..{name} your account created successfully..!!!")
                elif choice==2:
                    amount= int(input("Enter your amount for deposit :"))
                    current_user.deposit(amount)
                elif choice==3:
                    amount= int(input("Enter your amount for withdraw :"))
                    current_user.withdraw(amount)
                    
                elif choice==4:
                    current_user.check_available_balance()
                elif choice==5:
                    current_user.trsaction_history()
                    
                elif choice==6:
                    amount= int(input("Enter your amount for bank loan :"))
                    current_user.loan(amount)
                elif choice==7:
                    recipient=int(input("Enter your id for recipient..."))
                    amount= int(input("Enter your amount for transfer:"))
                    current_user.transfer(recipient,amount)
                elif choice==8:
                    break
                else:
                    print("Invalid choice.. Please choose valid choice in the option..")
                    break
                

    elif op==3:
        break
    
    
    