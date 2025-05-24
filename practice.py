# Q1
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via 
# a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def Display_details(self):
        return f"student name is {self.name}, and total marks is {self.marks}"
    
New_student = Student("Hassan" , 90)
print(New_student.Display_details())


# Q2
# Create a class Circle with an attribute radius. Write a method area() that returns the area of the circle. Use the value of π as 3.14.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        area = 3.14 * (self.radius ** 2)
        return f"the area off circle is {area}"
    
Get_area = Circle(12)
print(Get_area.Area())
print(Get_area.radius)


# Q3
# Create a class Person with attributes name and age. Add a method is_adult() that returns True if age is 18 or more, otherwise False.

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def Is_adult(self):

        if self.age >= 18:
            return "True , you are adult"
        else:
            return "False , you are under age"
        
New_Person = Person("Hassan" , 17)
print(New_Person.Is_adult())
print(New_Person.name)
print(New_Person.age)


# Q4
# Create a class BankAccount with attributes account_holder and balance. Add a method deposit(amount) to increase balance and display_balance() to print it.

class Bank_Account:
    def __init__(self, acount_holder , balance = 0):
        self.acount_holder = acount_holder
        self.balance = balance

    def deposit(self , amount):

        #two ways😅

        # self.amount = amount
        # balanceafterdeposit = self.balance + self.amount
        # self.balance = balanceafterdeposit

        self.balance += amount

        return f"{self.acount_holder} your new balance is {self.balance} after you deposit {amount}"
    
    def display_balance(self):
        return f"Hey !{self.acount_holder}, your current balnce is {self.balance}"
    


New_Account = Bank_Account("usman" , 500)
print(New_Account.balance) #500
print(New_Account.deposit(1000))
print(New_Account.balance) # 1500
print(New_Account.display_balance())




# Inheritance

# Q1
# Create a base class Animal with a method speak(). Create two subclasses Dog and Cat that override the speak() method with appropriate messages.

class Animal:
    def Speak(self):
        return "Animal Voice"
    
class Dog(Animal):
    def Speak(self):
         return "dog is barking !!!!"
    
class Cat(Animal):
    def Speak(self):
        return "cat is speaking ... Meow Meow!!"
    


my_pet = Animal()
print(my_pet.Speak())

your_pet = Dog()
print(your_pet.Speak())

hers_pet = Cat()
print(hers_pet.Speak())


# Q2
# Create a class Vehicle with attributes brand and model. Create a subclass 
# Car that inherits from Vehicle and adds an attribute seats. Add a method show_details() in Car.


class Vehicle:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self , brand , model , seats):
        super().__init__(model , brand)
        self.seats = seats

    def show_details(self):
        return f"""
                brand : {self.brand}
                Model of car is : {self.model}
                seats : {self.seats}
                """
    

my_car = Car( "800 s" ,"Teesla"  ,4)
print(my_car.show_details())


# Q3
# Define a base class Shape with a method area(). Create a subclass Rectangle that takes length and width, and implements the area() method

class shape:
    def __init__(self):
        pass

    def area():
        pass

class Rectangle(shape):
    def __init__(self , lenght , width):
        self.lenght = lenght
        self.width = width

    def area(self):
        Area = self.lenght * self.width 
        return f"Area of rectangle is {Area}"
    
shapes = Rectangle(2 ,3)
print(shapes.area())
print(shapes.lenght)
print(shapes.width)


# Encapsulation

# Q1
# Create a class Employee with private attributes __name and __salary. Add methods set_details(name, salary) and get_details() to update and return the values.


class Employee:
    def __init__(self , name , salary):
        self.__name = name
        self.__salary = salary

    def get_details(self):
        return f"name : {self.__name} , salary : {self.__salary}"
    
    def set_details(self , __name , __salary):
         self.__name = __name
         self.__salary = __salary


New_Employee = Employee("hassan" , 15000)
# print(New_Employee.__name)
# print(New_Employee.__salary)
print(New_Employee.get_details())
print(New_Employee.set_details("usman", 20000))
print(New_Employee.get_details())


