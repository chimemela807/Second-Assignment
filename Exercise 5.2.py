def create_account(name,initial_balance):
    return{
        "name":name,
        "balance":initial_balance,
        "history":[],
        "day_counter":0
    }
def perform_transaction(account,amount,transaction_type):
    """Deposits or withdraws money, with overdraft protection on withdrawals"""
    if amount<=0:
        print("Amount must be greater than zero❗")
        return False
    
    account["day_counter"]+=1
    date_label=(f"Day{account['day_counter']}")
    if transaction_type=="deposit":
        account["balance"]+=amount
        account["history"].append((date_label,"deposit",amount))
        print(f"Deposited ₦{amount:.2f}.New balance:₦{account['balance']:.2f}")
        return True
    elif transaction_type=="withdraw":
        if amount>account["balance"]:
            print(f"Transaction declined:insufficent funds❕.Balance:₦{account['balance']:.2f}")
            account["day_counter"]-=1
            return False
        account["balance"]-=amount
        account["history"].append((date_label,"withdraw",amount))
        print(f"Withdrew ₦{amount:.2f}.New balance:₦{account['balance']:.2f}")
        return True
    else:
        print("Invalid transaction type. Use 'deposit' or 'withdraw'.")
        account["day_counter"]-=1
        return False
def show_transaction_history(account):
    print(f"\nTransaction History for {account['name']}")
    if not account["history"]:
        print("No transactions yet")
        return
    for date,t_type,amount in account["history"]:
        print(f"{date:6}|{t_type.upper():8}|₦{amount:.2f}")
        print("-"*40)
def monthly_summary(account):
    total_deposits=0
    total_withdrawals=0
    for date, t_type, amount in account["history"]:
        if t_type=="deposit":
            total_deposits+=amount
        elif t_type=="withdraw":
            total_withdrawals+=amount
    print(f"\n{'Monthly Summary for'+' ' +account['name']:^40}")
    print(f"Total Deposits:     ₦{total_deposits:.2f}")
    print(f"Total Withdrawals:  ₦{total_withdrawals:.2f}")
    print(f"Final Balance:      ₦{account['balance']:.2f}")

def main():
    name=input("Enter account name:")
    while True:
        try:
            initial_balance=float(input("Enter initial balance:₦"))
            if initial_balance<0:
                print("Initial balance cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    account=create_account(name,initial_balance)
    print(f"\nAccount created for {account['name']} with balance ₦{account['balance']:.2f}")
    while True:
        print(f"\n{'BANK MENU':^40}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Transaction History")
        print("4. Monthly Summary")
        print("5. Exit")
        menu=input("Choose an option(1-5):")
        if menu=="1":
            try:
                amount=float(input("Enter deposit amount:₦"))
                perform_transaction(account,amount,"deposit")
            except ValueError:
                print("Please enter a valid number.")
        elif menu=="2":
            try:
                amount=float(input("Enter withdrawal amount:₦"))
                perform_transaction(account,amount,"withdraw")
            except ValueError:
                print("Please enter a valid number.")
        elif menu=="3":
            show_transaction_history(account)
        elif menu=="4":
            monthly_summary(account)
        elif menu=="5":
            print(f"Thank you, {account['name']}. Final balance:₦{account['balance']:.2f}")
            break
        else:
            print("Invalid choice. Please select 1-5.")
if __name__=="__main__":
    main()