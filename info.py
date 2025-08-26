# class Info():
#     greet = "How are you doing?"


# print(Info)   


# info1 = Info()
# print(info1.greet)

# class Person():
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def __str__(self):
#         return f"FullName: {self.firstName} {self.lastName}"
    
#     # def user_details(self):
#     #     return f"Name: {self.firstName} {self.lastName}"
            

# p1 = Person("Korede", "Prince") 
# print(p1) 

#declaration of class and constructors
class Laptop():
    def __init__(laptop, brand, ROM, RAM, color, chip):
        laptop.brand = brand
        laptop.ROM = ROM
        laptop.RAM = RAM
        laptop.color = color
        laptop.chip = chip

    def __str__(laptop):
        return f"This laptop is a {laptop.brand} with {laptop.ROM} ROM and {laptop.RAM} RAM, it is {laptop.color} in color and has an {laptop.chip} chip"
    

l1 = (Laptop("MacBook 2020 pro", "256GB", "8GB", "silver gray", "Apple M1 Silicon"))
l2 = (Laptop("MacBook 2021 pro", "512GB", "16GB", "crimson red", "Apple M1 Silicon"))
l3 = (Laptop("MacBook 2022 pro", "720GB", "24GB", "forest green", "Apple M2 Silicon"))
l4 = (Laptop("MacBook 2023 pro", "900GB", "32GB", "deep sea blue", "Apple M3 Silicon"))
l5 = (Laptop("MacBook 2024 pro", "950GB", "50GB", "banana yellow", "Apple M4 Silicon"))
laptoplist = [l1, l2, l3, l4, l5]

for list in laptoplist:
    print(list)


#Inheritance
