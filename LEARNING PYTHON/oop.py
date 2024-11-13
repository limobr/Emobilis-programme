#Classes and objects

class Car:
    """A class for cars"""
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def drive(self):
        print(f"The {self.color} {self.model} is driving")

    