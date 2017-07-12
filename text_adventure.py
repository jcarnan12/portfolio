print("start")

from time import sleep
# delay the comp
sleep(2) # of seconds is the input

print("You're on your way to a party and you're running late! Since you are rushing, you end up getting lost. Which way should you go?\n")
sleep(2)
print("type left to left or right to go right")
user_input = input()
if user_input == "left":
    print("You decide to go left, which lands you in traffic!\n")
    sleep(2)
    print("keep going or go home?")
    user_input = input()
    if user_input == "keep going":
        print("You made it to the party! It's lit! \n")
        sleep(2)
        print("THE END.")
    elif user_input == "go home":
        print("Wrong choice! On the way home to your house, your car blows up and you die.\n")
        sleep(2)
        print("THE END.")

# different option!
if user_input == "right":
    print("It's your lucky day! The roads are clear. Although there is no traffic you're still not sure if you want to go. Do you keep going? \n")
    print("type yes to continue, type no to be lame and go home")
    sleep(2)
    user_input = input()
    if user_input == "yes":
        print("PARTY TIME! You made it to the party fashionably late and had a great time.\n")
        sleep(2)
        print("THE END.")
    elif user_input == "no":
        print("When you turn around to go home, you crash into another car and break your leg! Womp womp.\n")
        sleep(2)
        print("THE END.")
