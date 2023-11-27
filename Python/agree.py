s = input("Do you agree?")

# if s == "Y" or s == "y":
if s in ["Y", "y"]:
    print("Agreed")
elif s == "N" or s == "n":
    print("Not agreed")