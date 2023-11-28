text = "In the great green room"
words = text.split()


print ("Round 1")
for word in words:
    print(word)
print()

#Round 1
#In 
#the 
#great 
#green 
#room

print("Round 2")
for word in words:
    for c in word:
        print(c)

print()

#Round 2
#I
#n
#t
#h
#.
#.
#.


print("Round 3")
for word in words:
    if "g" in word:
        print(word)
print()

#Round 3
#great
#green


print("Round 4")
for word in words[2:]:
    print(word)
print()

#Round 4
#great
#green
#room

print("Round 5")
for word in words():
    #instead of word we can use _ (it means anything)
    print("Goodnight Moon")
print()

#Round 5
#Goodnight Moon
#Goodnight Moon
#Goodnight Moon
#Goodnight Moon
#Goodnight Moon

