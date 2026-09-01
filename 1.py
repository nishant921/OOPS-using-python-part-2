# Q1:Count number of instances of a class created in Python?
# Example: Say Car is any class.

# maruti = Car()
# bmw = Car()
# honda = Car()
# So after creating above instances. We want to count how many instances are created of Car class.

# For above example no of instances = 3.

# Write a program for above problem

class Car:

    __no_of_instances = 0
    def __init__(self):
        self.__car_name = ''
        Car.__no_of_instances+=1
        self.__car_id = Car.__no_of_instances

    @staticmethod
    def get_count_instances():
         return Car.__no_of_instances
   
    def set_name(self,name):
        self.__car_name = name 

    def get_car_name(self):
        return self.__car_name
    def get_car_id(self):
        return self.__car_id

maruti = Car()
bmw = Car()
honda = Car()
maruti.set_name('maruti')
print(maruti.get_car_name())
print(maruti.get_car_id())

bmw.set_name('bmw')
print(bmw.get_car_name())
print(bmw.get_car_id())

honda.set_name('honda')
print(honda.get_car_name())
print(honda.get_car_id())

# print(Car._Car__no_of_instances) good to know but don't do 
print(Car.get_count_instances())
    