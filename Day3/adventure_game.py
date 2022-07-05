print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input(
    "You see two paths in front of you. The right one leads you to a dark forest. The left path leads you to a lake. Which path do you choose? \n"
).lower()

road_final = ""

if road.find("left") != -1 and road.find("right") == -1:
    print("You chose to go left.")
    road_final = "left"
elif road.find("right") != -1 and road.find("left") == -1:
    print("You chose to go right.")
    road_final = "right"
else:
    road2 = input(
        "Sorry I didn't catch that. Which path do you choose? Please type 'right' or 'left' \n"
    ).lower()
    while (road2.find("left") == -1 and road2.find("right") == -1) or (
        road2.find("left") != -1 and road2.find("right") != -1
    ):
        road2 = input(
            "Sorry I didn't catch that. Which path do you choose? Please type 'right' or 'left' \n"
        ).lower()

    if road2.find("left") != -1 and road2.find("right") == -1:
        print("You chose to go left.")
        road_final = "left"
    elif road2.find("right") != -1 and road2.find("left") == -1:
        print("You chose to go right.")
        road_final = "right"
