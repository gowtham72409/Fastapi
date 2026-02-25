

# NUMBER GUESSING GAME


# import random
# print("WELCOME ! our number guessing game $ ")
# print("Please select the option")
# print("1.Easy - (1-50) range,7 attempt")
# print("2.Medium - (1-100) range,10 attempt")
# print("3.hard - (1-500) range,5 attempt")

# c=input("Enter the choice (1/2/3):")

# if c=="1":
#     c=random.randint(1,50)
#     attempt_left=7
# elif c=="2":
#     c=random.randint(1,100)
#     attempt_left=10
# elif c=="3":
#     c=random.randint(1,500)
#     attempt_left=5
# else:
#     print("\n Choice is wrong!Default medium level")
#     c=random.randint(1,100)
#     attempt_left=10

# print("strat game")
# while attempt_left > 0:
#     try:
#         guess=int(input("Enter the number:"))
#         attempt_left-=1

#         if guess > c:
#             print("Too high")
#         elif guess < c:
#             print("Too low")
#         else:
#             print("winner")
#             break

#         print("Attempt_left:",attempt_left)

#     except ValueError:
#         print("Invalid number!Please enter valid number")

# if attempt_left==0 and guess!=c:
#     print("Game over!The number was:",c)

# print("Thank you")

# SIMPLE CALCULATE

# print("WELCOME! calculator")

# print("1.Addition\n2.subbraction\n3.Multiplication\n4.Division\n5.Power")
# n=input("Enter the choice(1/2/3/4/5):")

# n1=int(input("Enter the number1:"))
# n2=int(input("Enter the number2:"))

# if n=="1":
#     result=n1+n2
#     print("Result:",result)

# elif n=="2":
#     result=n1+n2
#     print("Result:",result)

# elif n=="3":
#     result=n1*n2
#     print("Result:",result)

# elif n=="4":
#     if n2==0:
#         print("Error:This number not divisible by zero")
#     else:
#         result=n1/n2
#         print("Result:",result)

# elif n=="5":
#     result=n1**n2
#     print("Result:",result)

# else:
#     print("Invalid option")


# PALINDROME

# def palindrome(text):
#     l=text.replace(" ","").lower()
#     return l == l[::-1]

# a=input("Enter the string:")
# print(palindrome(a))

# word frequency counter

# import re
# from collections import Counter

# para=input("Enter the paragraph:")
# para=para.lower()
# p=re.findall(r'\b\w+\b',para)
# word_counter=Counter(p)
# top_5=word_counter.most_common(5)

# print("\nTop 5 repeat word")
# for word,count in top_5:
#     print(f"{word}:{count}")

# password check 

# import re 

# def password_check(password):
#     length=len(password)>=8
#     upper=re.search(r'[A-Z]',password)
#     lower=re.search(r'[a-z]',password)
#     digit=re.search(r'[0-9]',password)
#     special=re.search(r'[A-Za-z0-9]',password)

#     s=sum([bool(length),bool(upper),bool(lower),bool(digit),bool(special)])

#     if s<=2:
#         return "weak"
#     elif s==3 or s==5:
#         return "medium"
#     else:
#         return "strong"
    
# password=input("Enter the password:")
# print("Password_strength:",password_check(password))

# Bank (oop)

class BankAccount:
    def __init__(self,account_no,account_holder,balance=0):
        self.account_no=account_no
        self.account_holder=account_holder
        self.balance=balance
        self.transaction=[]

    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            self.transaction.append(f"Deposited :{amount}")
            print(f"{amount}.RS Deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self,amount,):
        if amount<=0:
            print("Invalid amount")
        elif amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            self.transaction.append(f"withdraw :{amount}")
            print(f"{amount}.RS Withdraw successfully")

    def check_balance(self):
        print(f"Current balance:{self.balance}")

    def show_transaction(self):
        print("\nTransaction History")
        if not self.transaction:
            print("No Transaction")
        else:
            for t in self.transaction:
                print(t)

class Bank:
    def __init__(self):
        self.account={}
    
    def create_account(self,account_no,account_holder):
        if account_no in self.account:
            print("Account number already exist")

        else:
            self.account[account_no] = BankAccount(account_no,account_holder)
            print("Account successfully created")

    def get_account(self,account_no):
        return self.account.get(account_no,None)

bank=Bank()

while True:
    print("\n==== Banking System ====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    pin=int(input("Enter the pin:"))

    if pin==2324:

        choice=input("choose the option:")

        if choice=="1":
            acc_no=input("Enter account number:")
            name=input("Enter the account holder:")
            bank.create_account(acc_no,name)

        elif choice in ["2","3","4","5"]:
            acc_no=input("Enter account number:")
            account=bank.get_account(acc_no)

            if account:
                if choice=="2":
                    amount=float(input("Enter deposite amount:"))
                    account.deposite(amount)
                elif choice=="3":
                    amount=float(input("Enter withdraw amount:"))
                    account.withdraw(amount)
                elif choice=="4":
                    account.check_balance()
                elif choice=="5":
                    account.show_transaction()
            else:
                print("Account not found")

        elif choice == "6":
            print("Thank you for using the banking system.")
            break

        else:
            print("Invalid choice. Please try again.")
    else:
        print("Invalid pin")
            


