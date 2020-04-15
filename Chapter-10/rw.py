import json

filename = 'numbers.json'

try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
        print("The user like number is :" + number + ".")

except FileNotFoundError:
    number = input("What is your like number ?")
    with open(filename,"w") as f_obj:
        json.dump(number, f_obj)

