from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def vehicle_info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def start_engine(self):
        return f"{self.vehicle_info()} engine started with key"

    def stop_engine(self):
        return f"{self.vehicle_info()} engine stopped"

class Motorcycle(Vehicle):
    def start_engine(self):
        return f"{self.vehicle_info()} engine started with button"

    def stop_engine(self):
        return f"{self.vehicle_info()} engine turned off"

car = Car("Toyota", "Corolla")
bike = Motorcycle("Yamaha", "R1")

print(car.start_engine())
print(car.stop_engine())
print(bike.start_engine())
print(bike.stop_engine())
