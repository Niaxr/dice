import random
i = random.randint(1, 6)
print("a random number between 1 and 6")
print(i)
answer = input("are you happy with this number? yes/no")

if answer == "yes":
    print("okay then")
    
else: print("too bad")
