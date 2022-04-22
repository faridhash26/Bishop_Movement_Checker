import numpy as np
import tkinter as tk   # PEP8: `import *` is not preferred
from chess_board import chess_locations, chess_name_number


# --- main ---


chess_alephabet = chess_locations.copy()


def show_chess_board(start=None, end=None):
    rows = 8
    cols = 8
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

    window = tk.Tk()
    for c in range(1, cols+1):
        l = tk.Label(window, text=str(c))
        l.grid(row=0, column=c)

    all_entries = []
    for r in range(len(chess_alephabet)):
        entries_row = []
        l = tk.Label(window, text=letters[r])
        l.grid(row=r+1, column=0)
        for c in range(len(chess_alephabet[r])):
            e = tk.Entry(window, width=3)  # 5 chars

            print( 'cond', (chess_name_number[r][c][0], str(chess_name_number[r][c][1])))
            if end == (chess_name_number[r][c][0], str(chess_name_number[r][c][1])):
                print( 'end',end)
                e.insert('end', "E")
                e.grid(row=r+1, column=c+1)
                entries_row.append(e)
                continue
            if start == (chess_name_number[r][c][0], str(chess_name_number[r][c][1])):
                e.insert('end', "S")
                e.grid(row=r+1, column=c+1)
                entries_row.append(e)
                continue
            
            e.insert('end', chess_alephabet[r][c][2])
            e.grid(row=r+1, column=c+1)
            entries_row.append(e)
        all_entries.append(entries_row)

    window.mainloop()
