import tkinter as tk
from tkinter import messagebox

#Check for a winner
def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]): #Row check
            return True
        if all([board[j][i] == player for j in range(3)]): #Column check
            return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: #Diagonal check
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player: #Diagonal check
        return True
    
    return False

#Check if the board is full (draw)
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

#button click
def button_click(row, col):
    global current_player
    
    if board[row][col] != " ":
        return  
    
    #Update board
    board[row][col] = current_player
    buttons[row][col].config(image=x_image if current_player == "X" else o_image, state="disabled")
    
    #Print who is winner
    if check_winner(board, current_player):
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        reset_game()
        return
    
    #Print if its a draw
    if is_full(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()
        return
    
    #Switch player and update whose turn
    current_player = "O" if current_player == "X" else "X"
    update_turn_label()

#Reset the game
def reset_game():
    global current_player, board
    current_player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(image=empty_image, state="normal")
    
    update_turn_label()

#Update the label (whose turn)
def update_turn_label():
    if current_player == "X":
        turn_label.config(text="Player X's Turn", fg="blue")
    else:
        turn_label.config(text="Player O's Turn", fg="red")

#Initialise the window
root = tk.Tk()
root.title("Tic-Tac-Toe")

#Load images
x_image = tk.PhotoImage(file="x_image.png")  
o_image = tk.PhotoImage(file="o_image.png")  
empty_image = tk.PhotoImage(file="empty_image.png")  
restart_image = tk.PhotoImage(file="restart_button.png")  

#Initialise game state
current_player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]

#Create buttons for the grid
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, image=empty_image, width=100, height=100,
                                  command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

#Create restart button
restart_button = tk.Button(root, image=restart_image, command=reset_game)
restart_button.grid(row=3, column=0, columnspan=2)

#Create label to show turn
turn_label = tk.Label(root, text=f"Player {current_player}'s Turn", font=("Arial", 9), fg="blue")
turn_label.grid(row=3, column=2)

root.mainloop()
