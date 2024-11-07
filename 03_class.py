class Employee:
    name = "Alif"
    language = "python"
    salary = 1300000


    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")
    
    def greet(self):
        print("Good Morning")

alif = Employee() # This is object
# alif.language = "JavaScript"
print(alif.language)
alif.greet()
# alif.getInfo()
Employee.getInfo(alif)