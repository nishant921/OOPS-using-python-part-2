# Q-4: Problem 4
# Statement: Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product. The program must display the years, months and days that are left for expiry.

import datetime

class Product:
    def __init__(self):
        self.__product = input("Enter Product Name: ")
        self.__manufacture = input("Enter Manufacturing Date (MM/DD/YY): ")
        self.__expiry = input("Enter Expiry Date (MM/DD/YY): ")

        try: 
            self.__manufacture = datetime.datetime.strptime(self.__manufacture,"%m/%d/%y")
            self.__expiry = datetime.datetime.strptime(self.__expiry,"%m/%d/%y")
        except ValueError:
            self.__manufacture = datetime.datetime.strptime(self.__manufacture,"%m/%d/%Y")
            self.__expiry = datetime.datetime.strptime(self.__expiry,"%m/%d/%Y")

    def time_to_expiry(self):
        curr=datetime.datetime.now()

        if curr>self.__expiry:
            print("Product already expired!")

        else:
            days = (self.__expiry.date() - curr.date()).days
            years = days // 365
            months = (days % 365) // 30
            remaining_days = (days % 365) % 30

            print(f"Time left: {years} years, {months} months, {remaining_days} days")


p1=Product()
p1.time_to_expiry()