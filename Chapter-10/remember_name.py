import json

# def greet_user():
#     filename = 'user_names.json'
#
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("What is your name ?")
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print("We will remember you when come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")
#
#
# greet_user()


def get_stored_username():
    filename = 'user_names.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_name():
    usename = input("What is your name ?")
    filename = 'user_names.json'
    with open(filename, 'w') as f_obj:
        json.dump(usename, f_obj)
    return  usename

def greet_user():
    username = get_stored_username()
    cur_name = input("The use name ' " + username + " ' is your name ? (yes/no) ")
    if cur_name == 'yes':
        print("Welcome back, " + username + "!")
    else:
        username = get_new_name()
        print("We'll remember you when you come back, " + username + "!")

greet_user()