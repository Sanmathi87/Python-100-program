account = {
    "name": input("Enter account holder name: "),
    "balance": float(input("Enter initial balance: "))
}

def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account["balance"] += amount
    print("Deposited:", amount)
    print("Current Balance:", account["balance"])

def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient balance")
    print("Current Balance:", account["balance"])

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        deposit(account)
    elif choice == "2":
        withdraw(account)
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
