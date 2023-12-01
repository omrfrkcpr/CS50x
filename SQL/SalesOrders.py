import csv

with open("SalesOrders.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        favorite = row["Region"]
        print(favorite)