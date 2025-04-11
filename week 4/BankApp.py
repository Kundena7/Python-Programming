def credit(bal,amount,transcation):
    bal+=amount
    print(amount,"credited successfully")
    transcation.append(amount)
    return bal,transcation
def debit(bal,amount,transcation):
   if bal< amount:
       print("Insufficient balance")
   else:
         bal-=amount
         print(amount,"debited successfully")
         transcation.append(-amount)
         return bal,transcation
def checkbal(bal):
    print(bal)
def last_transaction(transaction):
    print("Last transaction")
    for x in transaction:
        print(x)
   




bal=0
transaction=[]
while True:
    print("Welcome to BankApp")
    print("Press 1 to credit")
    print("press 2 to debit")
    print("press 3 to check balance")
    print("press 4 to check last  transaction")
    print("press 5 to Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        amount=int(input("Enter amount to credit:"))
        bal,trabsaction=credit(bal,amount,transaction)
    elif choice==2:
        ampount=int(input("Enter amount to debit:"))
        bal,transaction=debit(bal,amount,transaction)
    elif choice==3:
        checkbal(bal)
    elif choice==4:
        last_transaction(transaction)
    elif choice==5:
        print("Thank You using BankApp")
        break
    else:
        print("Invalid choice")
