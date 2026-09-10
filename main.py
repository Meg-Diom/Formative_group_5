#!/usr/bin/env python3

from data import *
from transactions import *
from savings import *
from reports import *


def main():

    data = load_data()

    transactions = data["transactions"]
    saving_goals = data["saving_goals"]

    user_id = input("Enter your user ID: ")
    user_name = input("Enter your name: ")

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
            spending_type = input("Enter income/expense: ")
            spending_details = input("Enter spending details: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date: ")
            description = input("Enter description: ")

            add_transactions(
                transactions,
                user_id,
                user_name,
                spending_type,
                spending_details,
                amount,
                date,
                description
            )

        elif choice == "2":
            view_transaction(transactions, user_id)

        elif choice == "3":
            results = search_transaction(transactions, user_id)

            if not results:
                print("No transactions found.")
            else:
                for transaction in results:
                    print(transaction)

        elif choice == "4":
            spending_details = input("Enter spending details: ")
            amount = float(input("Enter amount: "))
            field = input("Enter field to update: ")
            modify = input("Enter new value: ")

            update_transaction(
                transactions,
                user_id,
                spending_details,
                amount,
                field,
                modify
            )

        elif choice == "5":
            spending_details = input("Enter spending details: ")
            amount = float(input("Enter amount: "))

            result = delete_transaction(
                transactions,
                user_id,
                spending_details,
                amount
            )

            print(result)

        elif choice == "6":
            budget_summary(transactions, user_id)

        elif choice == "7":
            goals = input("Enter savings goal: ")
            target = float(input("Enter target amount: "))

            add_savings_goal(
                saving_goals,
                user_id,
                user_name,
                goals,
                target
            )

        elif choice == "8":
            view_savings_goals(saving_goals, user_id)

        elif choice == "9":
            saving_progress(
                transactions,
                user_id,
                saving_goals
            )

        elif choice == "10":
            month = input("Enter month (YYYY-MM): ")

            monthly_summary(
                transactions,
                user_id,
                month
            )

        elif choice == "11":

            data["transactions"] = transactions
            data["saving_goals"] = saving_goals

            save_data(data)

            print("Data saved successfully.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
