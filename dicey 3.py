import random

again = True
x = 0

while again:
    die = int(input("how many die do u want?"))
    while x < die:
        x += 1
        i = random.randint(1, 6)
        print(i)
    again = input("Again? True/False")
    
