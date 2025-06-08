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



# Create a class `Vector` with `x` and `y`. Override the `+`  operator (`__add__`)
#  to add two vectors. Override `__str__` to return a nice string like `"Vector(2, 3)"`.





class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Example usage:
v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2

print(v1)  # Output: Vector(2, 3)
print(v2)  # Output: Vector(4, 1)
print(v3)  # Output: Vector(6, 4)
