# Q-3: Find the area of a rectangle.
# Approach:

# The class name should be Rectangle.
# The constructor should accept two parameters length and height but you can't pass the values directly to it while creating the constructor. E.g., rectangle = Rectangle(length=10, height=8) <-- you can't do that while creating the instances.
# Create a method called area() which has no parameters.
# Create a method called is_square() which also has no parameters. Return True if the rectangle is a square otherwise return False.
# If you are using a if-else block inside the is_square() method, then use the one-linear syntax.


class Rectangle:

    def __init__(self,length,height):
        self.length = length
        self.height = height

    @classmethod
    def property(cls,len,bre):
        return cls(len,bre)

    def area(self):
        return self.height*self.length

       
    def is_square(self):
        return self.height==self.length

r1=Rectangle.property(8,8)
print(r1.area())
print(r1.is_square())