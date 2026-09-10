#!/usr/bin/env python3

def add_transactions(transactions, user_id, user_name, spending_type, spending_details, amount, date, description):
    new_transaction = {
        "user_id": user_id,
        "user_name": user_name,
        "spending_type": spending_type,
        "spending_details": spending_details,
        "amount": amount,
        "date": date,
        "description": description
    }
    transactions.append(new_transaction)
    return transactions

def search_transaction(transactions, user_id):
    results = []

    for transaction in transactions:
        if transaction["user_id"] == user_id:
            results.append(transaction)

    return results

def view_transaction(transactions, user_id):
    results = search_transaction(transactions, user_id)
    
    if not results:
        print("No Transactions yet")
        return

    print(f"{'='*25}\nTRANSACTION HISTORY\n{'='*25}")
    for result in results:
        print(result)
        print(f"{'='*25}")

def update_transaction(transactions, user_id, spending_details, amount, field, modify):
    results = search_transaction(transactions, user_id)

    for transaction in results:
        if transaction.get("amount") == amount and transaction.get("spending_details") == spending_details:
            transaction[field] = modify
    return transactions

def delete_transaction(transactions, user_id, spending_details, amount):
    results = search_transaction(transactions, user_id)
    
    for transaction in results:
        if transaction.get("spending_details") == spending_details and transaction.get("amount") == amount:
            transactions.remove(transaction)
            return transactions
    return "Transaction Not Found!"

def filter_transaction(transactions, field, value):
    results = []

    for transaction in transactions:
        if transaction.get(field) == value:
            results.append(transaction)

    return results

def budget_summary(transactions, user_id):
    results = search_transaction(transactions, user_id)

    total = 0
    for transaction in results:
        # print "detail: amount"
        print(f"{transaction.get('spending_details')}: {transaction.get('amount')}")
        total += transaction.get("amount", 0)
    return total

def saving_progress(transactions, user_id, total_income, saving_goals, goals, target):
    total_spending = budget_summary(transactions, user_id)

    results = []

    for saving_goal in saving_goals:
        if saving_goal.get("user_id") == user_id:
            results.append(saving_goal)
    if not results:
        return "Goal not found"
    for saving_goal in results:
        saving_goal["goals"] = goals
        saving_goal["target"] = target
        saving_goal["saved_amount"] = total_income - total_spending
        if saving_goal["target"]:
            saving_goal["progress"] = ((saving_goal["saved_amount"] / saving_goal["target"]) * 100)
        else:
            saving_goal["progress"] = 0.0
    return f"Goals: {saving_goal['goals']}\nTarget: {saving_goal['target']}\nSaved Amount: {saving_goal['saved_amount']}\nProgress: {saving_goal['progress']}"
