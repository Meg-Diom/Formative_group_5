#!/usr/bin/env python3

import json

def load_data():

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error: File not found!")
        return {"transactions": [
            {
            "user_id": None,
            "user_name": None,
            "spending_type": None,
            "spending_details": None,
            "amount": None,
            "date": None,
            "description": None
            }
        ], 
        "saving_goals": [
            {
            "user_id": None,
            "goals": None,
            "target": None,
            "saved_amount": None,
            "progress": None
            }
        ]
        }
    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return {"transactions": [
            {
            "user_id": None,
            "user_name": None,
            "spending_type": None,
            "spending_details": None,
            "amount": None,
            "date": None,
            "description": None
            }
        ],"saving_goals": [
        {
            "user_id": None,
            "goals": None,
            "target": None,
            "saved_amount": None,
            "progress": None
            }
            ]
        }
    
    except IOError:
        print("Error: Couldn't read this file!")
        return {"transactions": [
            {
            "user_id": None,
            "user_name": None,
            "spending_type": None,
            "spending_details": None,
            "amount": None,
            "date": None,
            "description": None
            }
        ], "saving_goals": [
            {
            "user_id": None,
            "goals": None,
            "target": None,
            "saved_amount": None,
            "progress": None
        }
        ]
        }
def save_data(data):

    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        print("Error: Could not save file!")

