import json

file_name = 'user_names.json'

with open(file_name) as name:
    username = json.load(name)
    print("Welcome back, " + username + "!")