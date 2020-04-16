import print_functions
from print_functions import make_car
from print_functions import make_car as mc
import print_functions as mcar

car1 = print_functions.make_car('subaru', 'outback', color='blue', tow_package=True)
car2 = make_car('subaru', 'outback', color='blue', tow_package=True)
car3 = mc('subaru', 'outback', color='blue', tow_package=True)
car4 = mcar.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)
print(car2)
print(car3)
print(car4)