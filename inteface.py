import tkinter as tk
from tkinter import ttk
import constants as con
import sounds

def draw_fretboard(event=None):
    canvas.delete("all")  # Wyczyść poprzednie linie

    window_width = canvas.winfo_width()
    window_height = canvas.winfo_height()
    
    # Oblicz odstępy
    vertical_space = (window_width - con.LEFT_SPACE - con.RIGHT_SPACE) / (con.FRETS_NUMBER - 1)
    horizontal_space = vertical_space / con.RATIO

    canvas.create_text(10, 10, text="Scaler", anchor="nw", font=("Arial", 16, "bold"), fill="blue")

    # Rysuj wybrane dźwięki 
    pos = sounds.isolate_notes("STANDARD", "PENTATONIC", tonation_button.get(), sounds_position())
    for note, x, y in pos:
            r = horizontal_space / 2
            canvas.create_oval(x-r, y-r, x+r, y+r, fill="lightblue", outline="black", width=0)


    # Rysuj poziome linie
    for i in range(con.STRINGS_NUMBER):
        y = window_height - con.DOWN_SPACE - i * horizontal_space 
        canvas.create_line(con.LEFT_SPACE, y, window_width - con.RIGHT_SPACE, y, width=2, fill="black")

    # Rysuj pionowe linie (ograniczone do obszaru poziomych linii)
    for j in range(con.FRETS_NUMBER):
        x = j * vertical_space + con.LEFT_SPACE
        grubość = 4 if j == 0 else 1  # Pierwsza pionowa linia grubsza

        fret_start = window_height - con.DOWN_SPACE - (con.STRINGS_NUMBER - 1) * horizontal_space
        canvas.create_line(x, fret_start, x, window_height - con.DOWN_SPACE , width=grubość, fill="black")
        if j != 0:
            canvas.create_text(x - vertical_space / 2, window_height - con.DOWN_SPACE , text=f"{j}", anchor="n", font=("Arial", 10), fill="black")

def sounds_position():
    window_width = canvas.winfo_width()
    window_height = canvas.winfo_height()

    vertical_space = (window_width - con.LEFT_SPACE - con.RIGHT_SPACE) / (con.FRETS_NUMBER - 1)
    horizontal_space = vertical_space / con.RATIO

    positions = {}

    for i in range(con.STRINGS_NUMBER):
        positions[window_height - con.DOWN_SPACE - i * horizontal_space] = [] 

    for j in range(con.FRETS_NUMBER):
        x = j * vertical_space + con.LEFT_SPACE
        for pos in positions.values():
            pos.append(int(x - vertical_space / 2))
    return positions

def tonation_change(event):
    draw_fretboard()

# --- Tworzenie głównego okna ---
window = tk.Tk()
window.title("Siatka linii reagująca na rozmiar okna")
window.geometry("1000x400")

#==========================================================
#======  comboboxy  =======================================
#==========================================================

frame = tk.Frame(window)
frame.pack(side="top", anchor="nw", padx=10, pady=10)

# --- combobox ze skalami ---

scale_button = ttk.Combobox(frame, values=list(con.SCALES.keys()), state="readonly")
scale_button.set("PENTATONIC")  
scale_button.pack(pady=5, padx=10, side="left")
scale_button.bind("<<ComboboxSelected>>", tonation_change)


# --- combobox z tonacjami ---

tonation_button = ttk.Combobox(frame, values=con.NOTES, state="readonly")
tonation_button.set("C")  
tonation_button.pack(pady=5, padx=10, side="left")
tonation_button.bind("<<ComboboxSelected>>", draw_fretboard)


# --- Tworzenie canvasu ---
canvas = tk.Canvas(window, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# --- Automatyczne rysowanie przy zmianie rozmiaru okna ---
window.bind("<Configure>", draw_fretboard)

# --- Pierwsze rysowanie ---
def start():
    draw_fretboard()
    window.mainloop()

