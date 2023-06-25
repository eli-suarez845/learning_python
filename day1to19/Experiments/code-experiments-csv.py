import csv  # process CSB files

with open("../Bonus/files/weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])

# Enter a city: New York
#  "20"

