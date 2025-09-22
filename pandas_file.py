import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
# print(df)


examData = {
    "Name": ["Mike", "David", "Daniel", "Korede", "Stephanie", "Frank"],
    "Study Hours": [5, 3, 8, 2, 7, 4],
    "Sleep Hours": [7, 6, 6, 5, 8, 7],
    "Score": [80, 60, 92, 55, 88, 72] 
}

edf = pd.DataFrame(examData)
# print(edf)

# print(edf.info)
# print(edf.describe)

new_date = pd.read_csv("data.csv")
# print(new_date.head())
print(new_date.tail())