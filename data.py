#!/usr/bin/env python3

import json

def load_data():

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error: File not found!")
        return {"transactions": [], "saving_goals": []}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return {"transactions": [], "saving_goals": []}

    except IOError:
        print("Error: Couldn't read this file!")
        return {"transactions": [], "saving_goals": []}

def save_data(data):

    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        print("Error: Could not save file!")

