# name = 'zion'
# print(name[0])

#     print(school)

# print(len(school))

#how to check if port of exists w
# if "port" in school:
#     print("pleace specify, which of the port?")

# else:
#     print("BACKSHOTS")

#slicing
message = "This is the place"
# print(message[12:]) #slicing from beginning
# print(message[:4]) #slicing from the end

# print(message.upper()) #converting to upper case
# print(message.lower()) #converting to lower case

# msg = "      hello"
# print(len(msg.strip()))  #to strip away white space, called trim in other languages

ex = "Uche, Bimbo, Mario"
# print(ex.replace("Bimbo", "Ada")). #to replace a value in a string with smth else

# newStr = ex.split(",") #converting a sring to into a list

#Formatting a string
friend = "Zion"
# print(f"my friends name is {friend}"). #formatting print and yes the f at the beginning is necessary
# txt = f"The most handsome guy in our class is the {friend}". #same thing sha, just without paranthesis
# print(txt)

# price = 45
# txt2 = f"The current price is {price: .2f} naira". to 2 decimal places
# print(txt2)

# quantity = 3
# unit_price = 400
# total_sale = f"Total: {quantity * unit_price}"
# print(total_sale).      #yes u can calculate arithmetic with it

# user_name = "daniel"
# print(user_name.capitalize()). converts the first letter to upper case

# account_number = "123345"
# print(account_number.isalpha()).  # checks if its a number of alphabet in the string

#reverse a string

# def reverseString(str):
#     return str[::-1]


# print(reverseString("Zion"))

# def checkPalindrome(str):
#     newstr = str[::-1]
#     if str == newstr:
#         return "Its a palindrome"
#     else:
#         return "it isnt a palindrome"
    

# print(checkPalindrome("ebube"))  


# def vowel_count(str):
#     vowels = "aeiouAEIOU"

#     return sum(1 for char in str if char in vowels)

# print(vowel_count("zion")) 