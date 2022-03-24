#Author: Tarek Mostafa Abo-Baker

print("                                     Welcome to the 100 game\n")
print("To start the game you have to enter a number between 1 to 10")
print("To end the game you have to reach the number 100")
print("First one reach 100 win\n")
print("Good luck\n")


nums = 0


# Display numbers
def display_state():
    global nums
    print("100/", nums)


# Get number the player wants to play
def get_input(player):
    valid = False
    while not valid:  # Repeat until a valid move is entered
        message = player + " player please enter the number between 1 and 10: "
        move = input(message)  # Get move as string

        if move.isdigit():  # If move is a number
            move = int(move)  # can take 1-10 number only
            if move in range(1, 11) and nums + move <= 100:
                valid = True
    return move


# Update numbers after the move
def update_state(nums_taken):
    global nums
    nums += nums_taken


# Check if he/she is taking the last move and loses
def is_win():
    global nums
    if nums > 99:
        return True


# define  the 100 game
def play__100_game():
    display_state()
    while (True):  # Repeat till one of them loses
        first = get_input("First")
        update_state(first)
        display_state()  # Display new numbers
        if (is_win()):
            print("First player won")
            break

        second = get_input("Second")
        update_state(second)
        display_state()
        if (is_win()):
            print("Second player won")
            break


play__100_game()

