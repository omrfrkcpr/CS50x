import csv

with open("SalesOrders.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    # East, Central, West = 0, 0, 0
    for row in reader:
        favorite = row["Region"]
        counts[favorite] += 1
        # if favorite == "Central":
        #     Central += 1
        # elif favorite == "East":
        #     East += 1
        # elif favorite == "West":
        #     West += 1

print(f"Central: {Central}")
print(f"East: {East}")
print(f"West: {Central}")