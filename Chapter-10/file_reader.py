file = 'guest_book.txt'
while True:
    with open(file, 'a', encoding='UTF-8') as file_object:

        name = input("Please inter your name:")
        print("Hello, " + name)
        file_object.write(name + ' visited \n')


