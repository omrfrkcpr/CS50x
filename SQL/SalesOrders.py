import csv

with open("SalesOrders.csv", "r") as file:
    reader = csv.reader(file)
    next(row)
    for row in reader:
        favorite = row[1]
        print(favorite)