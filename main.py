from message import getusername         #classic python import statement
import platform
from message import user
import datetime
import math
import json
from maths.geometry import areaofcircle
from Manager import Manager
from developer import Developer
from rest import Calculator

pf = dir(platform)
# print(pf)
# print(user["age"])

# dt = datetime.datetime.now()
# print(dt.strftime("%d"))         #getting day of the month

# print(math.pow(2, 4))

product = '{"name": "Hero", "age": 23, "city": "rivers"}'
pdc = (json.loads(product))
# print(type(pdc))

us = json.dumps(user)
# print(us.upper())


# emp1 = Manager("Nathan", 5000, "IT")
# emp2 = Developer("Prince", 2300, "HTML")

# emp1.show_details()
# print("-----------**-------------")
# print()
# emp2.show_details()

calc = Calculator()
print(calc.add(1,2,3,4,5,6,7))