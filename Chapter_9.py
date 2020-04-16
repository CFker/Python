# """9.1.1"""
# class Dog():
#     """一次模拟小狗的简单尝试"""
#
#     def __init__(self, name, age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟小狗被命令时蹲下"""
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         """模拟小狗被命令时打滚"""
#         print(self.name.title() + " rolled over!")
#
#
# my_dog = Dog('willie', 6)
#
# print(my_dog.name.title())
# print(my_dog.age)
# my_dog.sit()
# my_dog.roll_over()
#

# 9.1
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number
        print(str(self.number_served) + " person has luanch in restaurant.")

    def increment_number_served(self, numbers):
        self.number_served += numbers
        print("The restaurant can service " + str(self.number_served))

    def describe_restaurant(self):
        print("The restaurant name is :" + self.restaurant_name.title())
        print("The cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is opening")

restaurant = Restaurant('beijing fan dian', 'china')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(20)
restaurant.increment_number_served(10)
#
# class User():
#
#     def __init__(self, first_name, last_name, sex, tall, wight):
#
#         self.first_name = first_name
#         self.last_name = last_name
#         self.sex = sex
#         self.tall = tall
#         self.wight = wight
#
#     def describe_user(self):
#         print("The name is :" + self.first_name + ' ' + self.last_name)
#         print("sex is " + self.sex)
#         print("tall is " + self.tall)
#         print("wight is " + self.wight)
#
#     def greet_user(self):
#         print("Hello " + self.first_name + self.last_name)
#
# per_1 = User('chen', 'haha', 'man', '170', '150')
# per_1.describe_user()
# per_1.greet_user()

# class Car():
#     """一次模拟汽车的简单测试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 110
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def increment_odometer(self, miles):
#         """将里程碑按照读数增加指定的量"""
#         self.odometer_reading += miles
#
#     def update_odometer_reading(self, mileage):
#         """
#         将里程表读数设置为指定的数
#         禁止往回修改里程值
#         """
#         if mileage > self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("Stop! You can't roll back an odometer!")
#
#     def read_odometer_reading(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
# my_new_car = Car('audi', 'a8', 2020)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer_reading(50)
# my_new_car.increment_odometer(100)
# print (my_new_car.read_odometer_reading())