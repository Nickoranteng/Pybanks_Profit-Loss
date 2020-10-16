# create variables for player_one
player_one = "y"

# Set start and last number
starting_number = 0

# While we are still playing...
while player_one == "y":

    # input how many numbers
    players_choice = input("HOW MANY NUMBERS? ")

    # Loop through the numbers. 
    for x in range(starting_number, int(players_choice) + starting_number):

        # Print the number(s) in the range
        print(x)

    #  Set the next starting number as the last number of the previous loop
    starting_number = starting_number + int(players_choice)

    # player decide to continue or not
    player_one = input("do you want to Continue the chain: (y)es or (n)o? ")
