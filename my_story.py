class student:
    name = "Alif" # class attribute
    roll = 16
    home = "Kornai"


    def getInfo(self): 
        print(f"The name is {self.name}. The Roll Number is {self.roll}. The Home is {self.home}")

    def __init__(self):
        print(f"This boy name is {self.name}. The boy is working Now Coding") # dunder method
    

school = student()
# print(school.name, school.roll, school.home)

school.getInfo() # Object attribute