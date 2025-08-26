# a = 6
# print(a)
# print(a+4)

# print(2==2)
# print("mike" =="Mike")

# print(2!=1)
# > > >= <= 

# print(6>3)

# def add(a,b):
#     return a + b

# print(add(5,4))
# sum = add(67,90)

# print(f'sum = {sum}')

# def userAge(age):
#     if age < 18:
#         return 'You are not eligible'
#     return 'Congratulations'

# # print(userAge(90))

# def studentScore(score):
#     grade = ""
#     if score >=70 and score <=100:
#         grade = "A"
#     elif score <=60:
#         grade = "B"
#     elif score <=50:
#         grade = "C"
#     else:
#         grade="F"
#     return grade

# stdGrade = studentScore(60)

# prefix = ""

# if stdGrade=="A":
#     prefix = "An"

# print("You scored "+prefix+ " " +stdGrade)

# def simpleInterest(p, r, t):
#     return p * r * t

# result = simpleInterest(23, 2, 10)

# print('Simple Interest = {result}')

# def userAge(age):
#     if age < 18:
#         return 'You are not qualified to apply'
#     return "Congrats brodie"

# output = userAge(20)

# # print(output)

# balance = 0
# def ATM(input):
#     if input == 1:
#         amount = (2300)
        
# a = "mango"
# b = "orange"
# c = "lemon"

# friuts = ["mango","orange","lemon","watermelon"]
         #0         1         2      3

# print(friuts[0])
# size = len(friuts)
# print(size)
# last  = friuts[size - 1]

# print(last)

# def either6(values):
#     return values[0]==6 or values[len(values)-1]==6

# print(either6([34,6,2,3,1,6,23]))


# print(friuts[-1])

# print(friuts[1:])
# print(friuts[:2])
# print(friuts[-3])

# friuts[1] = "Apple"

# print(friuts)

friuts = ["mango","orange","lemon","watermelon"]
# friuts.insert(2,"Pineaple")

# friuts.append("banana")

# type2 = ["banana","pineaple"]

# friuts.extend(type2)

# friuts.remove("lemon")
# friuts.pop(2) #pop() remove last 

# del friuts[1]

friuts = ["mango","orange","lemon","watermelon"]

# print(friuts)

# for fruit in friuts:
#     print(fruit)


# for i in range(3):
#     print(friuts[i])

# [print(x) for x in friuts]
# print(friuts)


# def findLargest(values):
#     max = values[value]
#     for value in values:
#         if value[value+1] > value[value]:
#             value[value+1] = max

#     return max




# def findSum(values):
#     sum = 0
#     for value in values:
#        value += sum
#     if sum > 10000:
#         return "Alert, too heavy"
#     return "all good"
    




# def findExceed(values):
#     newvalue = []
#     for value in values:
#         if value > 5:
#             values+=newvalue
#             return newvalue
        





# def findShortestDays(values):
#     for value in values:
#         if value == 0 and value+1 == 0:
#             return value
        


# print(findShortestDays([[5,0,0,4,6,],[]]))


# def loopInner(values):
#     for value in values:
#         for innervalue in value:
#             return innervalue