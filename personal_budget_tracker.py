transactions = []
savings_goals = []


def add_transaction():
    pass


def view_transactions():
    pass


def search_transactions():
    pass


def update_transaction():
    pass


def delete_transaction():
    pass


def budget_summary():
    pass


def add_savings_goal():
    pass


def view_savings_goals():
    pass


def savings_progress():
    pass


def monthly_summary():
    pass


def main():

    while True:

        print("\n===================================")
        print(" PERSONAL BUDGET & SAVINGS TRACKER")
        print("===================================")
        print("1. Add Income / Expense")
        print("2. View Transactions")
        print("3. Search Transactions")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Budget Summary")
        print("7. Add Savings Goal")
        print("8. View Savings Goals")
        print("9. Savings Progress")
        print("10. Monthly Summary Report")
        print("11. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            search_transactions()

        elif choice == "4":
            update_transaction()

        elif choice == "5":
            delete_transaction()

        elif choice == "6":
            budget_summary()

        elif choice == "7":
            add_savings_goal()

        elif choice == "8":
            view_savings_goals()

        elif choice == "9":
            savings_progress()

        elif choice == "10":
            monthly_summary()

        elif choice == "11":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()