people = []
expenses = []

def add_person():
    name = input("Enter person name: ")
    people.append(name)
    print(f"{name} added!")

def add_expense():
    name = input("Who paid? ")
    amount = float(input("Amount: "))
    expenses.append({"paid_by": name, "amount": amount})
    print("Expense added!")

def show_summary():
    if not people:
        print("No people added.")
        return

    total = sum(exp["amount"] for exp in expenses)
    share = total / len(people)

    print("\n--- SUMMARY ---")
    print(f"Total Expense: {total}")
    print(f"Each person should pay: {share}")

    balances = {p: 0 for p in people}

    for exp in expenses:
        balances[exp["paid_by"]] += exp["amount"]

    print("\nBalances:")
    for person in balances:
        balance = balances[person] - share
        if balance > 0:
            print(f"{person} should get {balance}")
        else:
            print(f"{person} should pay {abs(balance)}")

while True:
    print("\n1. Add Person")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_person()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        break
    else:
        print("Invalid choice")