import random

def gamewin(computer, user) :
    if computer == user :
        return None
    elif (computer== "s" and user== "w") or (computer == "w" and user == "g") or (computer == "g" and user == "s" ) :
        return False
    else :
        return True
    
print ("WELCOME TO SNAKE WATER GUN GAME")
print ("CHOOSE AN OPTION :")
print ("1. Snake (s)")
print ("2. water (w)")
print ("3. Gun (g)")

choice = input ("ENTER YOUR CHOICE (1/2/3):")

if choice == "1":
    user = "s"
elif choice == "2" :
    user = "W"
elif choice == "3" :
    user = "g"
else:
    print ("Invalid input ! Please enter 1,2, or 3")
    exit()

#computer choice
randNo = random.randint(1,3)
if randNo == 1:
    computer = "s"
elif randNo == 2:
    computer = "w"
else :
    computer = "g"
 #result (not showing computer's choice)
print (f"You chose ; {user}")

result = gamewin(computer,user)

if result is None :
    print("It is a tie")
else:
    print("You Lose !")





