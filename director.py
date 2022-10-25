import random

def main():
    try:
        program = int(input("Would you like to run the program? (0=no or 1=yes) "))
        if program == 1:
            choice()
        elif program == 0:
            print("Thanks for playing :) ")
        else:
            print("Invalid number.")
            main()
    except ValueError as error:
        print("Please type 0 or 1")
        main()
        
    


def six_sided_dice():
    dice = random.randint(1,6)
    return dice

def ten_sided_dice():
    dice = random.randint(1,10)
    return dice

def twenty_sided_dice():
    dice = random.randint(1,20)
    return dice

def choose_dice():
    try:
        specific_dice = int(input("What dice would you like to roll (1=6sd, 2=10sd, 3=20sd)?  "))
        if specific_dice == 1:
            dice = six_sided_dice()
            print(f"You rolled a {dice}.")
            main()
        elif specific_dice == 2:
            dice = ten_sided_dice()
            print(f"You rolled a {dice}.")
            main()
        elif specific_dice == 3:
            dice = twenty_sided_dice()
            print(f"You rolled a {dice}.")
            main()
        else:
            print("Please pick a valid number.")
            choose_dice()
    except ValueError as error:
        print("Please pick a number.")
        choose_dice()

def choice():
    try:
        value = int(input("What would you like to do? (1-dice, 2-shop, 3-combat, 4-return to menu) "))
        if value == 1:
            choose_dice()
        elif value == 2:
            shop()
        elif value == 3:
            combat()
        elif value == 4:
            main()
        else:
            print("Please pick a valid number.")
            choice()
    except ValueError as error:
        print("Please pick a number (0 or 1 or 2 or 3).")
        choice()

def shop():
    answer = (input("Welcome to my shop! Would you like to hear what's on sale? "))
    if answer == "y":
        roll = six_sided_dice()
        if roll == 6:
            print("Today is your lucky day! Everything is 20 percent off!")
            store()
        else:
            print("Sadly, nothing is on sale today.")
            store()
    elif answer == "n":
        print("Sad to hear, but please take a look around.")
        store()
    else:
        print("Please enter 'y' or 'n' ")
        shop()

def combat():
    try:
        player_hp = int(input("How much health do you have? "))
        if player_hp < 0:
            print("Please type a valid number.")
            combat()
        else:
            print(f"You have {player_hp} hp")
        
        enemy_hp = int(input("How much health does your enemy have? "))
        if enemy_hp < 0:
            print("Please type a valid number.")
            combat()
        else:
            print(f"Enemy has {enemy_hp} hp")
    except ValueError as error:
        print("Please type in a number.")
        combat()
    main()

def store():
    sword_type = ["bronze", "silver", "gold"]
    sword_level = [1, 2, 3]
    sword_cost = [100, 250, 450]
    value = int(input("What sword would you like? (1,2,3) ")) - 1
    print(f"You want a {sword_type[value]} sword. \
You must be level {sword_level[value]} in order to buy it. \
It costs: {sword_cost[value]} gold.")
    main()


    

if __name__ == "__main__":
    main()