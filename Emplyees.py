class Employees():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")

    def calculate_bonus(self):
        return self.salary*0.05