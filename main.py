from message import getusername         #classic python import statement
import platform
from message import user
import datetime
import math
import json
from maths.geometry import areaofcircle

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
print(us.upper())