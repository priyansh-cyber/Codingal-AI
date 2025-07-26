import random
print("Welcomt to Number Guessing Game")
print("Direction: The AI have selected a number between 1-10 and you have to guess it within just 3 chances")
computer = random.randint(1,10)
chance = 3
while True:
    number = int(input("enter a number:"))
    chance = chance-1
    if(number!=computer):
        print("you have", chance, "left")
    if(number>computer):
        print("try lower number")
    if(number<computer):
        print("try higher number")
    if(number==computer):
        print("you won")
        break 
    if(chance==0):
        print("you lost")
        print(computer)
        break 
    

