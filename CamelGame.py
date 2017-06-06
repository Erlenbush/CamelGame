import random
# Here is my attempt at "The Camel Game"

# Printing out the instructions

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your ")
print("desert trek and out-run the natives!\n")

# Create a boolean called "done" and set it to false

done = False

# Create other misc variables

miles_traveled = 0
thirst = 0
camel_exhaustion = 0
native_travel_distance = -20
native_travel = 0
drinks_in_canteen = 5
# Create a while loop that will keep looping while done is False, and ask the user their choice

while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    if thirst >= 4 and thirst < 6:
        print("You are getting thirsty!")
    if thirst == 6:
        print("You died of thirst!")
        print("Game over")
        done = True
    user_choice = input("What is your choice? ")
# User chose to quit loop
    if user_choice.upper() == "Q":
        done = True
# User chose status check
    elif user_choice.upper() == "E":
        print("Miles Traveled: ", miles_traveled)
        print("Drinks available: ", drinks_in_canteen)
        print("The natives are ", miles_traveled - native_travel_distance, " miles behind you!")
# User chose to stop for the night
    elif user_choice.upper() == "D":
        camel_exhaustion = 0
        print("The camel praises you for your wonderful choice!")
        native_travel = random.randint(7,14)
        native_travel_distance = native_travel_distance + native_travel
# User chose to go full speed ahead!
    elif user_choice.upper() == "C":
        travel = random.randint(10, 20)
        miles_traveled = miles_traveled + travel
        print("You traveled ", travel, " more miles!")
        thirst += 1
        camel_exhaustion = camel_exhaustion + random.randint(1,3)
        native_travel = random.randint(7, 14)
        native_travel_distance = native_travel_distance + native_travel
# User chose the moderate speed option
    elif user_choice.upper() == "B":
        travel = random.randint(5, 12)
        miles_traveled = miles_traveled + travel
        print("You traveled ", travel, " more miles!")
        thirst += 1
        camel_exhaustion += 1
        native_travel = random.randint(7, 14)
        native_travel_distance = native_travel_distance + native_travel
# User has chosen to take a drink from their canteen
    elif user_choice.upper() == "A":
        if drinks_in_canteen >= 1:
            drinks_in_canteen -= 1
            thirst = 0
            print("You took a drink from your canteen! There are: ", drinks_in_canteen, " drinks left!")
        else:
            print("You have no drinks available!")
