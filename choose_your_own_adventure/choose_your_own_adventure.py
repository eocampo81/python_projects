name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross it? Type walk or swim: ").lower()

    if answer == "swim":
        print("You swam accross and are eaten my a sea monster.")
    elif answer == "walk":
        print("You walked for miles and ran out of water and died from thirst. You lose.")
    else:
        print("Not a valid option. You lose. ")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or go back. Type cross or back: ").lower()

    if answer == "back":
        print("You turn around and start walking back. On your way, a dragon swept down and burnt you to a crisp! You lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            print("You talk to the stranger and he gives you gold and a nice long sword to aid in your adventures. The stranger points you to the direction of the nearest town so you can rest. You win!")
        elif answer == "no":
            print("The stranger smiles as you pass by. The next think you know you feel wet pain as you fall to the ground and die. The stranger has cleaved your back with a long sword and stolen your money. You lose.")
        else:
            print("Not a valid option. You lose. ")
    else:
        print("Not a valid option. You lose. ")
else:
    print("Not a valid option. You lose. ")

