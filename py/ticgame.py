# import tkinter as tk
# from tkinter import messagebox
# import math

# # Create main window
# root = tk.Tk()
# root.title("Tic Tac Toe - AI")

# board = [[" " for _ in range(3)] for _ in range(3)]
# buttons = [[None for _ in range(3)] for _ in range(3)]

# # Check winner
# def check_winner(player):
#     # Rows
#     for row in board:
#         if all(cell == player for cell in row):
#             return True

#     # Columns
#     for col in range(3):
#         if all(board[row][col] == player for row in range(3)):
#             return True

#     # Diagonals
#     if all(board[i][i] == player for i in range(3)):
#         return True
#     if all(board[i][2 - i] == player for i in range(3)):
#         return True

#     return False


# def is_draw():
#     return all(cell != " " for row in board for cell in row)


# # Minimax AI
# def minimax(is_maximizing):
#     if check_winner("O"):
#         return 1
#     if check_winner("X"):
#         return -1
#     if is_draw():
#         return 0

#     if is_maximizing:
#         best_score = -math.inf
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == " ":
#                     board[i][j] = "O"
#                     score = minimax(False)
#                     board[i][j] = " "
#                     best_score = max(score, best_score)
#         return best_score
#     else:
#         best_score = math.inf
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == " ":
#                     board[i][j] = "X"
#                     score = minimax(True)
#                     board[i][j] = " "
#                     best_score = min(score, best_score)
#         return best_score


# def computer_move():
#     best_score = -math.inf
#     move = None

#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == " ":
#                 board[i][j] = "O"
#                 score = minimax(False)
#                 board[i][j] = " "
#                 if score > best_score:
#                     best_score = score
#                     move = (i, j)

#     if move:
#         row, col = move
#         board[row][col] = "O"
#         buttons[row][col]["text"] = "O"
#         buttons[row][col]["state"] = "disabled"


# def on_click(row, col):
#     if board[row][col] == " ":
#         board[row][col] = "X"
#         buttons[row][col]["text"] = "X"
#         buttons[row][col]["state"] = "disabled"

#         if check_winner("X"):
#             messagebox.showinfo("Game Over", "🎉 You Win!")
#             reset_game()
#             return

#         if is_draw():
#             messagebox.showinfo("Game Over", "It's a Draw!")
#             reset_game()
#             return

#         computer_move()

#         if check_winner("O"):
#             messagebox.showinfo("Game Over", "🤖 Computer Wins!")
#             reset_game()
#         elif is_draw():
#             messagebox.showinfo("Game Over", "It's a Draw!")
#             reset_game()


# def reset_game():
#     for i in range(3):
#         for j in range(3):
#             board[i][j] = " "
#             buttons[i][j]["text"] = ""
#             buttons[i][j]["state"] = "normal"


# # Create buttons
# for i in range(3):
#     for j in range(3):
#         btn = tk.Button(root, text="", font=("Arial", 30), width=5, height=2,
#                         command=lambda r=i, c=j: on_click(r, c))
#         btn.grid(row=i, column=j)
#         buttons[i][j] = btn

# # Restart button
# restart_btn = tk.Button(root, text="Restart", font=("Arial", 14),
#                         command=reset_game)
# restart_btn.grid(row=3, column=0, columnspan=3, sticky="we")

# root.mainloop()

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe - 2 Player")
root.configure(bg="#1e1e2f")

board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

current_player = "X"

# -------- Game Logic --------

def check_winner(player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def check_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))


def click(row, col):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        
        color = "#4cc9f0" if current_player == "X" else "#ff4c4c"
        buttons[row][col].config(text=current_player, fg=color, state="disabled")

        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"🎉 Player {current_player} Wins!")
            reset()
            return

        if check_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset()
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"


def reset():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            board[i][j] = ""
            buttons[i][j].config(text="", state="normal")


# -------- UI Styling --------

def on_enter(e):
    e.widget['background'] = "#2a2a40"

def on_leave(e):
    e.widget['background'] = "#2d2d44"


frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(padx=20, pady=20)

for i in range(3):
    for j in range(3):
        btn = tk.Button(frame,
                        text="",
                        width=6,
                        height=3,
                        font=("Segoe UI", 24, "bold"),
                        bg="#2d2d44",
                        fg="white",
                        activebackground="#3a3a5a",
                        bd=0,
                        command=lambda r=i, c=j: click(r, c))
        btn.grid(row=i, column=j, padx=8, pady=8)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        buttons[i][j] = btn

restart_btn = tk.Button(root,
                        text="Restart Game",
                        font=("Segoe UI", 14),
                        bg="#4361ee",
                        fg="white",
                        activebackground="#3f37c9",
                        bd=0,
                        command=reset)
restart_btn.pack(pady=10)

root.mainloop()

