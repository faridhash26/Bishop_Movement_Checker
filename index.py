import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox
from show_chess_board import show_chess_board
from chess_board import chess_locations
from locations_of_bishop import calculate_odd_even

ROOT = tk.Tk()
ROOT.withdraw()


start_position = simpledialog.askstring(title="First Position", prompt="Enter your First Position:")
end_position = simpledialog.askstring(title="Second Position", prompt="Enter your Second Position:")
number = int( simpledialog.askstring(title="Number", prompt="Enter your Number Position:"))


all_legal_even = calculate_odd_even(8)
all_legal_odd = []
right_positions = []
chess = chess_locations.copy()




for position_row in chess:
    for position_col in position_row:
        if not (position_col[0], position_col[1]) in all_legal_even:
            all_legal_odd.append((position_col[0], position_col[1]))
        



def calculate_number_of_movement(start, end, number):

    if abs(start[0] - end[0]) == abs(start[1] - end[1]) and number == 1:
        if start == end and number > 0:
            return False
        return True

    if (start[0] == end[0] or start[1] == end[1]) and 2 <= number:
        return True
    elif (start[0] != end[0] or start[1] != end[1]) and 2 <= number:
        return True

    return False


def move(start, end, move_number):
    letters = [("a", 1), ("b", 2), ("c", 3), ("d", 4),
               ("e", 5), ("f", 6), ("g", 7), ("h", 8), ]
    if len(start) != 2 or len(end) != 2:
        return False

    start = tuple(start)
    end = tuple(end)

    for letter in letters:
        if start[0] == letter[0]:
            start = (letter[1], int(start[1]))
            break
    else:
        return False

    for letter in letters:
        if end[0] == letter[0]:
            end = (letter[1], int(end[1]))
            break
    else:
        return False

    if start == end and number == 0:
        return True
    if start in all_legal_odd and end in all_legal_odd:
        return calculate_number_of_movement(start, end, number)
    if start in all_legal_even and end in all_legal_even:
        return calculate_number_of_movement(start, end, number)
    return False
res = move(start_position, end_position, number )
tkinter.messagebox.showinfo("your answer",f"{( start_position,end_position , number)} --> {res}")
show_chess_board(tuple(start_position),tuple(end_position ))

exit()



