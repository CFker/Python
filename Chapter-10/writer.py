import json

filename = 'numbers.json'

with open(filename,'w') as f_obj:
    number = input("Please inter your like number :")
    json.dump(number, f_obj)
