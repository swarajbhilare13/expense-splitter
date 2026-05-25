people = []
expenses = []
def add_person():
    name = input("Enter person name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    if name in people:
        print("Person already exists!")
        return
    people.append(name)
    print(f"{name} added!")

def add_expense():
    if not people:
        print("Add people first!")
        return
    name = input("Who paid? ").strip()
    if name not in people:
        print("Person not found!")
        return
    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    expenses.append({"paid_by": name, "amount": amount})
    print("Expense added!")

def show_summary():
    if not people:
        print("No people added.")
        return
    if not expenses:
        print("No expenses added.")
        return
    total = sum(exp["amount"] for exp in expenses)
    share = total / len(people)
    print("\nSUMMARY")
    print(f"Total Expense: {total:.2f}")
    print(f"Each person should pay: {share:.2f}")
    balances = {person: 0 for person in people}
    for exp in expenses:
        balances[exp["paid_by"]] += exp["amount"]
    print("\nBalances:")
    for person in balances:
        balance = balances[person] - share
        if balance > 0:
            print(f"{person} should get {balance:.2f}")
        elif balance < 0:
            print(f"{person} should pay {abs(balance):.2f}")
        else:
            print(f"{person} is settled up.")
while True:
    print("EXPENSE SPLITTER")
    print("1. Add Person")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Exit")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        add_person()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")