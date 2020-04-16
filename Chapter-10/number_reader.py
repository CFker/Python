import json

filename = 'numbers.json'

with open('numbers.json', 'r') as num:
    numbers = json.load(num)
print(numbers)
