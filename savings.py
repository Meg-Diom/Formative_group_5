#!/usr/bin/env python3

from reports import budget_summary

def saving_progress(transactions, user_id, saving_goals):

    balance = budget_summary(transactions, user_id)

    results = []

    for saving_goal in saving_goals:
        if saving_goal.get("user_id") == user_id:
            results.append(saving_goal)

    if not results:
        return "Goal not found"

    for saving_goal in results:
        saving_goal["saved_amount"] = balance

        if saving_goal["target"]:
            saving_goal["progress"] = (
                saving_goal["saved_amount"] /
                saving_goal["target"]
            ) * 100
        else:
            saving_goal["progress"] = 0.0

    return results
