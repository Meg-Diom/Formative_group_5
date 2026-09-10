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
    for result in results:
        print(f"{25*"="}\nTRANSACTION HISTORY\n{25*"="} {result}\n{25*"="}")

def update_transaction(transactions, user_id, spending_details, amount, field, modify):
    
    results = search_transaction(transactions, user_id)

    for transaction in results:
        if transaction["amount"] == amount and transaction["spending_details"] == spending_details:
            transaction[field] = modify
    return transactions

def delete_transaction(transactions, user_id, spending_details, amount):

    results = search_transaction(transactions, user_id)
    
    for transaction in results:
        if transaction["spending_details"] == spending_details and transaction["amount"] == amount:
            transactions.remove(transaction)
            return transactions
    return "Transaction Not Found!"

def filter_transaction(transactions, field, value):

    results = []

    for transaction in transactions:
        if transaction[field] == value:
            results.append(transaction)

    return results
