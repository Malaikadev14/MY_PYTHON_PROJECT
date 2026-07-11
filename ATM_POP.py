import json
print("Welcome to Malaika ATM!")


try:
    with open("ATM.json","r")as f:
        users=json.load(f)
    users={int(k):v for k,v in users.items()}
except FileNotFoundError:
    users={5490:[5000,[]],4321:[10000,[]],7777:[9000,[]]}
user_pin=int(input("Enter your PIN:"))
if user_pin in users:
    Balance, History=users[user_pin]
    
    while True:
        print("\n====MENU====")
        print("1.Withdraw")
        print("2.Deposit")
        print("3.Check Balance")
        print("4.Change PIN")
        print("5.Mini statement")
        print("6.Transfer money")
        print("7.Exit")
        choice=int(input("Choose option:"))
        if choice==1:
            amount=int(input("Enter amount to withdraw:"))
           
            if amount<100:
                print("Minimum withdrawal amount is 100")
            elif amount>Balance:
                print("Insufficient Balance!")
            else:
                Balance-=amount
                History.append(f"Withdrew: {amount}")
                print("Withdrawal succussful! ")
                print("Remaining Balance:",Balance)
            
        
        elif choice==2:
            amount=int(input("Enter amount to deposit:"))
            Balance+=amount
            History.append(f"Deposited: {amount}")
            print("Deposit successful!")
            print("New Balance:",Balance)
            

                
        elif choice==3:
            print("Your Balance:",Balance)
        elif choice==4:
            old_pin=int(input("Enter old PIN:"))
            if old_pin==user_pin:
                new_pin=int(input("Enter New PIN:"))
                if new_pin in users:
                    print("PIN already exist.Try another")
                else:
                    users[new_pin]=users.pop(user_pin)
                    user_pin = new_pin
                    print("PIN changed successfully!")
            else:
                print("Wrong old PIN!")       
        elif choice==5:
            print("___ Last 5 Transaction___")
            if len(History)==0:
                print("No Transaction yet")
            else:
                for t in History[-5:]:
                    print(t)
            print("_____________")
        elif choice==6:
            receiver_pin=int(input("Enter Receiver PIN:"))
            if receiver_pin not in users:
                print("Receiver PIN not found!")
            elif receiver_pin==user_pin:
                print("Cannot send to your own PIN!")
            else:
                amount=int(input("Enter amount to send:"))
                if amount > Balance:
                    print("Insufficient Balance!")
                else:
                    Balance-=amount
                    users[receiver_pin][0]+=amount
                    History.append(f"Sent {amount} to {receiver_pin}")
                    users[receiver_pin][1].append("Received {amount} from {user_pin}")
                    print(f"Transfer successful! Received {amount} to {receiver_pin}")
                    print(f"Your New Balance:{Balance}")
        
        elif choice==7:
            users[user_pin]=[Balance,  History]
            with open("ATM.json","w") as f:
                json.dump(users,f)
            print("Thankyou for using Malaika ATM!")
            break
        else:
            print("Invalid option!")
        
else:
    print("Wrong PIN!Access Denied.")