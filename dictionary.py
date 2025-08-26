

car = {
   "brand": "toyota",
   "model": "corolla",
   "year": "2020",
   "automatic_transmission": True,
   "color": ["red", "white", "blue"]
}

# print(car.get("model")) #getting a value based on key
# print(car.keys()) #returns all the keys as a list
# ky = car.keys()
# print(ky)     #getting the keys thru variable names

# car["tinted"] = ["factory", "grade 0", "grade 1"]       #adding a new value to the dictionary
# print(car)

# car_values = car.values()
# print(car_values)       #getting all the values

#to update the year
# if "year" in car:
#     car["year"] = 2025


# print(car)

#remove an item from a dictionary
# car.pop("model")
# del car["model"]
# print(car)

#deleting the whole dictionary
#del car

for x in car:
    if x.startswith("b"):
        result = x.upper()
        print(result)


#looping thru and printing the values
# for values in car.values():
#     print(values)

# for key in car.keys():
#     print(key)                #printing all the keys

# mycopy = car.copy()
# print(mycopy)                 #copying a dictionary

# my_copy = dict(car)
# print(car)


# user1 = {
#     "name": "Mario",
#     "gender": "Female",
#     "skills": ["HTML", "CSS", "JAVASCRIPT", "TIKTOK"]
# }

# user2 = {
#     "name": "Korede",
#     "gender": "Female"            #wrapping a dictionary inside ANOTHER dictionary, no idea why tf i would need this but who cares    
# }

# user3 = {
#     "name": "King",
#     "gender": "Male"
# }

# users = {
#     "first": user1,
#     "second": user2,
#     "third": user3
# }

# print(users)

# print(users["first"]["name"])     #getting a value inside a nested dictionary
# print(users["first"]["skills"][0])            #if there is another array like shi inside, this is a way u can get whats indside, like index accessing, type shi ig 

