from cs50 import sql

db = SQL("sqlite:///SalesOrders.db")

SalesOrders = input("SalesOrders: ")

rows = db.execute("SELECT * FROM SalesOrders WHERE Religion = 'West'")

for row in rows:
    print(row["Items"])