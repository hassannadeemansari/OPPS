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

# class Bank_Account:
#     def __init__(self, acount_holder , balance = 0):
#         self.acount_holder = acount_holder
#         self.balance = balance

#     def deposit(self , amount):

#         #two ways😅

#         # self.amount = amount
#         # balanceafterdeposit = self.balance + self.amount
#         # self.balance = balanceafterdeposit

#         self.balance += amount

#         return f"{self.acount_holder} your new balance is {self.balance} after you deposit {amount}"
    
#     def display_balance(self):
#         return f"Hey !{self.acount_holder}, your current balnce is {self.balance}"
    


# New_Account = Bank_Account("usman" , 500)
# print(New_Account.balance) #500
# print(New_Account.deposit(1000))
# print(New_Account.balance) # 1500
# print(New_Account.display_balance())




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
        super().__init__(brand , model)
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

    def area(self):
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


# Q2
# Create a class Laptop with a private attribute __price. Use getter and setter
#  methods to access and modify __price with proper validation (e.g., price must be > 0).


class Laptop:
    def __init__(self, __price):
        self.__price = None
        self.set_price(__price)

    def get_price(self):
        return f"{self.__price}"
    
    def set_price(self , set_price):
        if set_price > 0 :
            self.__price = set_price
        else:
            return "invalid amount"
        
My_laptop = Laptop(30000)
print(My_laptop.get_price())
l1 = Laptop(-10)
print(l1.get_price())
print(My_laptop.get_price())
print(My_laptop.set_price(-10))
print(My_laptop.set_price(0))
My_laptop.set_price(500) 
print(My_laptop.get_price())
# print(My_laptop.__price)  private


# Q3
# Define a class Book with protected attribute _title. Create a subclass Ebook that
#  inherits from Book and accesses the protected _title in its method display().

class Book:
    def __init__(self , _title):
        self._title = _title


class Ebook(Book):
    def __init__(self , _title):
        super().__init__(_title)

    def display(self):
        return f"The title of book is {self._title}"
    
my_book = Book("Agentic Ai")
print(my_book._title)

mynew_book = Ebook("Generative AI")
print(mynew_book.display())


# Q4
# Create a base class Employee with a method get_role().
# Create subclasses Manager and Developer that override get_role() with their specific roles.
# Then, write a function print_role(emp) that takes any employee object and calls get_role().


class Employee:
    def __init__(self):
        pass

    def get_role(self):
        pass

class Manager(Employee):
    def get_role(self):
        return "Manage All Account and manage all Employees"



class Developer(Employee):
    def get_role(self):
        return "Mange all the development side work in company"


# def print_role(emp):
#     print(emp.get_role())

# e1 = Manager()
# e2 = Developer()

# print_role(e1)
# print_role(e2)



# Composition (Has-A Relationship)
# Create a class Engine with attribute horsepower.
# Create a class Car that has a brand and an Engine object.
# Add a method car_info() that prints car brand and engine horsepower.

class Engine:
    def __init__(self , horsepower):
        self.horsepower = horsepower

class Car(Engine):
    def __init__(self ,   brand ,horsepower ):
        super().__init__(horsepower)
        self.brand = brand

    def car_info(self):
        print(f"The brand of car is : {self.brand} and , its horsepower is : {self.horsepower}hps")

my_car = Car("bugatti" , 1500)
my_car.car_info()


# Bank System (Encapsulation + Validation + Methods)
# Create a class BankAccount with private attributes __account_holder, __balance.

# Add methods to deposit(), withdraw(), and get_balance().
# Validate that withdrawal can't exceed balance.
# Use getter/setter with proper validation.

class BankAccount:
    def __init__(self , accountholder , balance):
        self.__accountholder = accountholder
        self.__balance = 0
        if balance <= 0:
            raise ValueError("Initial balnce must be greater then 0")
        self.Deposit(balance)


    def Deposit(self , amount):

        if amount > 0:
            self.__balance += amount
            return f"{self.__accountholder} after you deposit {amount}, your balnce become {self.__balance}"
        
        else:
            return "invalid amount!"


    def Withdraw(self , amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"{self.__accountholder} you withdraw {amount} "
        else :
            return "insufficient funds"

        

    def get_balance(self):
        return f"{self.__accountholder} your current balance is {self.__balance}"
    
new_account = BankAccount("Usman" , 50000)
# print(new_account.Deposit(-100000000))
print(new_account.get_balance())
print(new_account.Withdraw(5000))
print(new_account.get_balance())



# for better experience..
#  Suggested Improvement:
# Wrap object creation in a try...except block:

# python
# Copy
# Edit
# try:
#     new_account = BankAccount("Usman", -50000)
# except ValueError as e:
#     print("Account creation failed:", e)


#  4. Library System (Multiple Classes)
# Book class with title, author, and is_borrowed.

# Library class with a list of books.
# Methods to add, borrow, and return books.
# Print available books.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                return f"You borrowed '{book.title}'"
        return "Book not available"

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                return f"You returned '{book.title}'"
        return "Book was not borrowed"

    def list_available_books(self):
        available = [f"{book.title} by {book.author}" for book in self.books if not book.is_borrowed]
        return "\n".join(available) if available else "No books available"


library = Library()

book1 = Book("Clean Code", "Robert C. Martin")
book2 = Book("The Pragmatic Programmer", "Andy Hunt")
book3 = Book("Atomic Habits", "James Clear")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.list_available_books())
print(library.borrow_book("Atomic Habits"))
print(library.list_available_books())
print(library.return_book("Atomic Habits"))
print(library.list_available_books())
