#!/usr/bin/env python3

from transactions import search_transaction


def budget_summary(transactions, user_id):
    results = search_transaction(transactions, user_id)

    total_income = 0
    total_expenses = 0

    for transaction in results:
        print(
            f"{transaction.get('spending_details')}: "
            f"{transaction.get('amount')}"
        )

        if transaction.get("spending_type") == "income":
            total_income += transaction.get("amount", 0)

        elif transaction.get("spending_type") == "expense":
            total_expenses += transaction.get("amount", 0)

    balance = total_income - total_expenses

    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Balance: {balance}")

    return balance