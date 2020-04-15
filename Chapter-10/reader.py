import json

filename = 'numbers.json'

with open(filename) as f_obj:
    number = json.load(f_obj)
    print("I like your favorite number! It's " + number + ".")