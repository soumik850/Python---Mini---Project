import random

target = random.randint(1, 100)

while True :
    userchoice = input("Guess the target or Quit :")
    if (userchoice == "Quit") :
        break

    userchoice = int(userchoice)
    if (target ==  userchoice) :
        print("Coreect Guess : Well Done")
        break
    elif (userchoice < target):
        print ("your number was too small")

    else:
        print("Your number was too big")

print ("GAME OVER")
    

