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

if road_final == "right":
    print("You went into the forest...")
    tiger = input(
        "A tiger leapt from the bushes. You can either fight the tiger or run to the lake where it can't follow. Will you fight or run? \n"
    ).lower()
    if tiger.find("fight") != -1 and tiger.find("run") == -1:
        print("You chose to fight.")
        tiger_final = "fight"
    elif tiger.find("run") != -1 and tiger.find("fight") == -1:
        print("You chose to run.")
        tiger_final = "run"
    else:
        tiger2 = input(
            "Sorry I didn't catch that. Will you fight or run? Please type 'fight' or 'run' \n"
        ).lower()
        while (tiger2.find("fight") == -1 and tiger2.find("run") == -1) or (
            tiger2.find("fight") != -1 and tiger2.find("run") != -1
        ):
            road2 = input(
                "Sorry I didn't catch that. Will you fight or run? Please type 'fight' or 'run' \n"
            ).lower()

        if tiger2.find("fight") != -1 and tiger2.find("run") == -1:
            print("You chose to go fight.")
            tiger_final = "fight"
        elif tiger2.find("run") != -1 and tiger2.find("fight") == -1:
            print("You chose to go run to the lake.")
            tiger_final = "run"
    if tiger_final == "fight":
        print("Game Over. You were no match for the tiger. You died.")
    else:
        print("You reach the lake side...the tiger didn't follow.")
        lake = input(
            "You can see the treasure chest across the other side of the lake. You can go across by walking on an old bridge in front of you or by swimming. Will you use the bridge or swim? \n"
        ).lower()
        if lake.find("bridge") == -1 and lake.find("swim") != -1:
            print("You chose to swim.")
            lake_final = "swim"
        elif lake.find("swim") == -1 and lake.find("bridge") != -1:
            print("You chose to use the bridge.")
            lake_final = "bridge"
        else:
            lake2 = input(
                "Sorry I didn't catch that. Will you use the bridge or swim? Type 'bridge' or 'swim'. \n"
            ).lower()
            while (lake2.find("swim") == -1 and lake2.find("bridge") == -1) or (
                lake2.find("swim") != -1 and lake2.find("bridge") != -1
            ):
                lake2 = input(
                    "Sorry I didn't catch that. Will you use the bridge or swim? Type 'bridge' or 'swim' \n"
                ).lower()
            if lake2.find("swim") != -1 and lake2.find("bridge") == -1:
                print("You chose to swim.")
                lake_final = "swim"
            elif lake2.find("bridge") != -1 and lake2.find("swim") == -1:
                print("You chose to use the bridge.")
                lake_final = "bridge"
        if lake_final == "swim":
            print(
                "Game Over. There were sea serpents in the lake and they ate you alive. You died."
            )
        else:
            print("Congratulations! You found the treasure! You Win!")
else:
    print("You reach the lake side...")
    lake = input(
        "You can see the treasure chest across the other side of the lake. You can go across by walking on an old bridge in front of you or by swimming. Will you use the bridge or swim? \n"
    ).lower()
    if lake.find("bridge") == -1 and lake.find("swim") != -1:
        print("You chose to swim.")
        lake_final = "swim"
    elif lake.find("swim") == -1 and lake.find("bridge") != -1:
        print("You chose to use the bridge.")
        lake_final = "bridge"
    else:
        lake2 = input(
            "Sorry I didn't catch that. Will you use the bridge or swim? Type 'bridge' or 'swim'. \n"
        ).lower()
        while (lake2.find("swim") == -1 and lake2.find("bridge") == -1) or (
            lake2.find("swim") != -1 and lake2.find("bridge") != -1
        ):
            lake2 = input(
                "Sorry I didn't catch that. Will you use the bridge or swim? Type 'bridge' or 'swim' \n"
            ).lower()
        if lake2.find("swim") != -1 and lake2.find("bridge") == -1:
            print("You chose to swim.")
            lake_final = "swim"
        elif lake2.find("bridge") != -1 and lake2.find("swim") == -1:
            print("You chose to use the bridge.")
            lake_final = "bridge"
    if lake_final == "swim":
        print(
            "Game Over. There were sea serpents in the lake and they ate you alive. You died."
        )
    else:
        print("Congratulations! You found the treasure! You Win!")
