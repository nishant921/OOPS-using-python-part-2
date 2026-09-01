# Q-6: Ice-Cream Scoops and Bowl shop
# Create a class Scoop which has one public property flavour and one private proptery price. Take flavour values during object creation.

# Create a class Bowl with private prperty scoop_list which will have list of scoopd object.

# Create a method add_scoops in Bowl class which will add any no of Scoop objects given as parameter and store it in scoops_list.

# Make getter and setter method for price property.

# Make a method display to display flavour and price of each Scoop in scoop_list and print total price of the bowl by adding all flavour scoops prices.

# Make a method sold in both Scoop class and Bowl class to print no of quantity sold.


# Q-7:Ice-Cream Bowl continue..
# Making advancement in the above classes. Scoop and Bowl

# Introduce a property max_scoops in Bowl class to signify maximum scoops that a bowl can have, exceeding that it will display Bowl is full. Take default value as 3.

# no_of_scoop in Scoop class with default value of 1
# Print <flavour> added with every scoop added.

class Scoop:
     
    __counter = 0

    def __init__(self,flavour,scoop=1):
        self.flavour = flavour
        self.__price = None
        print(self.flavour,"added")
        self.no_of_scoop=scoop
        Scoop.__counter+=1

    def __str__(self):
        return "flavour- {}, No_of_scoops- {}, price- {}".format(self.flavour,self.no_of_scoop,self.__price)

    def set_price(self,price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    @staticmethod
    def sold():
        return Scoop.__counter

class Bowl:
    __counter = 0

    def __init__(self,max_scoop=3):
        self.__scoop_list = []
        self.max_scoops=max_scoop
        self.scoop_added=0
        Bowl.__counter += 1

    def add_scoops(self,*no_scoops):    
        for scoop in no_scoops:
            if self.scoop_added + scoop.no_of_scoop <= self.max_scoops:
                self.__scoop_list.append(scoop)
                self.scoop_added +=scoop.no_of_scoop
            else:
                print("Bowl is full")

    def display(self):
        total = 0
        for scoop in self.__scoop_list:
            print(scoop)
            total = total + scoop.get_price()*scoop.no_of_scoop
        print("Total Price: ",total)

    @staticmethod
    def sold():
        return Bowl.__counter

choco=Scoop('chocoloate',1)
choco.set_price(60)

vanilla = Scoop('vanilla',3)
vanilla.set_price(50)

berry = Scoop('berry')
berry.set_price(100)

print(choco,vanilla,berry,sep='\n')
print(Scoop.sold())

b1=Bowl()
b1.add_scoops(choco,vanilla)
b1.display()
print(Bowl.sold())