# Q-5: Problem 5
# Statement: A university wants to automate their admission process. Students are admitted based on the marks scored in the qualifying exam. A student is identified by student id, age and marks in qualifying exam. 

# Data are valid, if:
# Age is greater than 20
# Marks is between 0 and 100 (both inclusive)
# A student qualifies for admission, if

# Age and marks are valid and
# Marks is 65 or more
# Write a python program to represent the students seeking admission in the university. The details of student class are given below.

class Student:
    def __init__(self):
        self.__student_id = None
        self.__age = None
        self.__marks = None

    # setter methods
    def set_id(self):
        self.__student_id = int(input("Student ID: "))

    def set_age(self):
        self.__age = int(input("Age: "))

    def set_marks(self):
        self.__marks = int(input("Marks: "))

    # getter methods
    def get_id(self):
        return self.__student_id
    
    def get_age(self):
        return self.__age
    
    def get_marks(self):
        return self.__marks

    # Validations
    def validate_marks(self):
        return self.__marks in range(0,101)
        
    def validate_age(self):
        return self.__age>20
        
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            return self.__marks>=65
        else:
            return False


s1=Student()
s1.set_id()
s1.set_age()
s1.set_marks()

print(s1.get_id())
print(s1.get_age())
print(s1.get_marks())

print(s1.check_qualification())

