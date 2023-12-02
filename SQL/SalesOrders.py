import csv

with open("SalesOrders.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    # East, Central, West = 0, 0, 0
    for row in reader:
        favorite = row["Item"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# def get_value(Item):
#     return counts[Item]

for favorite in sorted(counts, key=lambda Item: counts[Item], reverse=True):
    print(f"{favorite}: {counts[favorite]}")

        # if favorite == "Central":
        #     Central += 1
        # elif favorite == "East":
        #     East += 1
        # elif favorite == "West":
        #     West += 1

# print(f"Central: {Central}")
# print(f"East: {East}")
# print(f"West: {Central}")

