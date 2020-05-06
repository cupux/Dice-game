import random
import time

# creating virtual names
virtual_names = ["Virtual Joseph", "Virtual Enyonam", "Virtual Esther", "Virtual Gifty",
                 "Virtual Akosoa", "Virtual Philip", "Virtual Sammy"]

# the max and min of the random numbers
min = 1
max = 6


x = 0
y = 0
print('''
 \t\t   -----------------------------------------
 \t\t   |                                       |
 \t\t   |       WELCOME TO MY DICE GAME         |
 \t\t   |                                       |
 \t\t   -----------------------------------------
''')

# player entering his name
player_name = input("Please enter your name: ")
upper_name = player_name.upper()


# function of the final score
def score(x,y):
    if x == y:
        print()
        print('''
         \t\t   -----------------------------------------
         \t\t   |                                       |
         \t\t   |            It's a draw.               |
         \t\t   |                                       |
         \t\t   -----------------------------------------
        ''')
        time.sleep(1)
        print()
        print("\nInput 'yes' to play again or 'no' to stop playing.")
        print()

    elif x > y:
        print()
        print('''
         \t\t   -----------------------------------------
         \t\t   |                                       |
         \t\t   |       You Won, Congratulations!       |
         \t\t   |                                       |
         \t\t   -----------------------------------------
        ''')
        time.sleep(1)
        print()
        print("\nInput 'yes' to keep playing OR 'no' to stop playing.")

        print()

    elif x < y:
        print()
        print('''
         \t\t   -----------------------------------------
         \t\t   |                                       |
         \t\t   |           Sorry! You Lost             |
         \t\t   |                                       |
         \t\t   -----------------------------------------
        ''')
        time.sleep(1)
        print()
        print("\nInput 'yes' to keep playing OR 'no' to stop playing.")
        print()


# function for the dice
def dice(d):
    if d == 1:
        print(""" 
      _________
     |         |
     |         |  
     |    *    | 
     |         | 
     |_________|  """)

    elif d == 2:
        print("""
      _________
     |         |
     |     *   |
     |         | 
     |   *     | 
     |_________|  """)

    elif d == 3:
        print("""
      _________
     |         |
     |      *  |  
     |    *    | 
     |  *      | 
     |_________|  """)

    elif d == 4:
        print("""
      _________
     |         |
     |  *   *  |  
     |         | 
     |  *   *  | 
     |_________|  """)


    elif d == 5:
        print(""" 
      _________
     |         |
     |  *   *  |  
     |    *    | 
     |  *   *  | 
     |_________|  """)


    elif d == 6:
        print("""   
      _________
     |         |
     |  *   *  |  
     |  *   *  | 
     |  *   *  | 
     |_________|  """)


# randomly looping through the virtual name list
for name in random.sample(virtual_names, 1):
    virtual_name = name
    virtual_name = virtual_name.upper()


# open_game = True
while True:
    start = input("Please type yes to start or no to play next time %s: " % upper_name)
    if start == "yes":
        roll_again = "yes"

        # starting the game
        while roll_again == "yes":
            if roll_again == "no":
                exit(0)
            print()
            time.sleep(1)
            print("\nYour Turn")
            time.sleep(1)
            print()
            print("\nDie is rolling...")

            time.sleep(2)

            x = random.randint(min, max)
            y = random.randint(min, max)

            dice(x)

            time.sleep(1)
            print()
            print("\n")
            print(virtual_name + "'s", ("Turn"))
            time.sleep(1)
            print()
            print("\nDie is rolling...")
            time.sleep(2)

            dice(y)

            time.sleep(1)
            score(x, y)

            roll_again = input(f"\nWould you like to roll the die again, {upper_name}? ")

    elif start == "no":
        print('''
         \t\t   -----------------------------------------
         \t\t   |                                       |
         \t\t           THANKS FOR PLAYING %s           
         \t\t   |                                       |
         \t\t   -----------------------------------------
        ''' % upper_name)
        exit(0)

    else:
        print("Wrong input")










