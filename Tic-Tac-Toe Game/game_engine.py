""" This Module contains all functions that controls the Tic-Tac-Toe Game
"""


def print_dashboard(dashboard):
    """Prints the Dashboard"""
    print(f"""
    ========================
       {dashboard[0][0]}   ||   {dashboard[0][1]}   ||   {dashboard[0][2]}
    ++++++++++++++++++++++++
       {dashboard[1][0]}   ||   {dashboard[1][1]}   ||   {dashboard[1][2]}
    ++++++++++++++++++++++++
       {dashboard[2][0]}   ||   {dashboard[2][1]}   ||   {dashboard[2][2]}
    ========================
    """)

def get_player_move():
    """Get valid player move"""
    while True:
        try:
            row = int(input("Select row (0 - 2): "))
            col = int(input("Select column (0 - 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Please choose values between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter integers.")

def play_game():
    """Perform the game function"""
    dashboard = [["" for _ in range(3)] for _ in range(3)]
    player = 'X'
    print_dashboard(dashboard)

    while True:
        print(f"Player {player}, it's your turn.")
        row, col = get_player_move()
        if dashboard[row][col] == "":
            dashboard[row][col] = player
            print_dashboard(dashboard)
            if check_winner(dashboard):
                print(f"Player {player} is the winner!!!")
                break
            elif check_draw(dashboard):
                print("DRAW!!!")
                break
            player = '0' if player == 'X' else 'X'
        else:
            print("Cell already taken. Try again.")

def check_winner(dashboard):
    """Check rows, columns, and diagonals for a win"""
    for i in range(3):
        if dashboard[i][0] == dashboard[i][1] == dashboard[i][2] != "":
            return True
        if dashboard[0][i] == dashboard[1][i] == dashboard[2][i] != "":
            return True
    if dashboard[0][0] == dashboard[1][1] == dashboard[2][2] != "":
        return True
    if dashboard[0][2] == dashboard[1][1] == dashboard[2][0] != "":
        return True
    return False

def check_draw(dashboard):
    """Checks if the game is a draw"""
    for i in range(3):
        for j in range(3):
            if dashboard[i][j] == "":
                return False
    return True