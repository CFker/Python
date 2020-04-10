
# prompt = "\nPlease enter the age of you:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# Active = True
# while Active:
#     age = input(prompt)
#     if age == 'quit':
#         Active = False
#         # break
#     elif 3 <= int(age)  <= 12:
#         print('The ' + str(age) + ' old year is $10')
#     elif int(age) > 12:
#         print('The ' + str(age) + ' old year is $15')
#     elif int(age) < 3:
#         print('The ' + str(age) + ' old year is free')

# numb = 0
# while numb < 10:
#     print('You are da SB')

# unconfig_users = ['Allen', 'tim', 'brian']
# config_users = []
# while unconfig_users:
#     user = unconfig_users.pop()
#     print("Verifying user: " + user.title())
#     config_users.append(user)
# print("\nThe follow users have been confirmed:")
# for config_user in config_users:
#     print(config_user.title())

#-----问卷调查-------
# responses = {}
# Active = True
# while Active:
#     name = input("\nWhat is your name ?")
#     response = input("Where would you like to visit ?")
#     responses[name] = response
#     repeat = input("Would you like to let another person respond? (yes / no)")
#     if repeat == 'no':
#         Active = False
#     elif repeat == 'yes':
#         Active = True
# print("\n--- Results ---")
# for name, response in responses.items():
#     print(name.title() + " would like to visit the  " + response.title() + ".")

#---三明治----
# sandwich_orders = ['apple', 'banner', 'tomato', 'pastrami', 'pastrami', 'orange', 'pastrami', 'pastrami']
# finished_sandwiches =[]
# print("The beer all sals out!")
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print("\nI made your " + sandwich + "sandwich.")
#     finished_sandwiches.append(sandwich)
# print("\n--- The made sandwich ---")
# for sandwiched in finished_sandwiches:
#     print(sandwiched)

#---牛肉----
# sandwich_orders = ['apple', 'banner', 'tomato', 'pastrami', 'pastrami', 'orange', 'pastrami', 'pastrami']
# finished_sandwiches =[]
# print("The beer all sals out!")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#     print("The pastrami is del")
# print("\n--- The made sandwich ---")
# for sandwich in sandwich_orders:
#     print(sandwich)

# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name:")
#     l_name = input("Last_name:")
#     for_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + for_name + "!")

#---音乐专辑----
# def make_album(songer, album, num = ''):
#     if num:
#         album = {'名字': songer.title(), '专辑': album, '数量': num}
#     else:
#         album = {'名字': songer.title(), '专辑': album, }
#     return album
# albums = []
# while True:
#     print("\nPlease enter songer name and album")
#     print("Enter 'q' quit .")
#     album_songer = input("album songer name:")
#     if album_songer == 'q':
#         break
#     album_name = input("album name:")
#     if album_name == 'q':
#         break
#     album_number = input("album number:")
#     if album_number == 'q':
#         break
#     albums.append(make_album(album_songer, album_name, album_number))
# print("\n--- The result ---")
# for i in albums:
#     print(i)

def get_users(names):
    for name in names:
        print("Hello, " + name.title() + "!")
users_name = ['ken', 'rola', 'Kim', 'herry']
get_users(users_name)