# Q1 Using self:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.



class Student():
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def Details(self):
        return(f"""Student Name : {self.name}
Total Marks = {self.marks} """)
        
NewStudent = Student("Hassan" , 80)
print(NewStudent.Details())







# Q3  3. Public Variables and Methods
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car():
    def __init__(self , brand):
        self.brand = brand

    def Start(self):
        return f"The Engine of {self.brand} is started!!"
    

class NewCar(Car):
    def __init__(self, brand):
        super().__init__(brand)
        self.brand = brand

    def start(self):
        return f"{self.brand} is ready to drive ..."
    

cl1 = Car("civic")
print(cl1.Start())


cl2 = NewCar("lamborgini")
print(cl2.start())