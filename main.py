import random

while True:
    dice = input("""Enter the Amount & type of die to roll 
(or 'exit' to quit)|1d4|2d6|3d8|4d10|5d12|6d20|7d100|> """)
    print("\n")
    if dice.lower() == 'exit':
        break
    try:
        amount = int(dice[0])
        sides = int(dice[2:])
        if sides in [4, 6, 8, 10, 12, 20, 100]:
            for amount in range(amount):
                result = random.randint(1, sides)
                print(f"You rolled a {result}")
            
            print("\n")
        else:
            print("Invalid die type. Please enter one of the following: d4, d6, d8, d10, d12, d20, d100.")
    except ValueError:
        print("Invalid input. Please enter a valid die type (e.g., d6) or 'exit' to quit.")

        