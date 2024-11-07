class Employee:
    name = "Alif"
    language = "Python"
    salary = 120000

    def getInfo(self):
        print(f"The name is {self.name}. The Language is {self.language}. The Salary is {self.salary}")

# job = Employee()

job_datelis = Employee()

print(job_datelis.name, job_datelis.language)

Employee.getInfo(job_datelis)