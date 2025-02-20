import tkinter as tk
from tkinter import ttk
import constants as con
import sounds


def draw_fretboard(event=None):
    canvas.delete("all")  

    # Oblicz odstępy
    window_width = canvas.winfo_width()
    window_height = canvas.winfo_height()
    vertical_space = (window_width - con.LEFT_SPACE - con.RIGHT_SPACE) / (con.FRETS_NUMBER - 1)
    horizontal_space = vertical_space / con.RATIO

    canvas.create_text(10, 10, text="Scaler", anchor="nw", font=("Arial", 16, "bold"), fill="blue")

    # Rysowanie poziomych linii (progi)
    for i in range(con.STRINGS_NUMBER):
        y = window_height - con.DOWN_SPACE - i * horizontal_space 
        canvas.create_line(con.LEFT_SPACE, y, window_width - con.RIGHT_SPACE, y, width=2, fill="black")

    # Rysowanie pionowych linii (struny)
    for j in range(con.FRETS_NUMBER):
        x = j * vertical_space + con.LEFT_SPACE
        grubość = 4 if j == 0 else 1  # Pierwsza pionowa linia grubsza

        fret_start = window_height - con.DOWN_SPACE - (con.STRINGS_NUMBER - 1) * horizontal_space
        canvas.create_line(x, fret_start, x, window_height - con.DOWN_SPACE , width=grubość, fill="black")
        if j != 0:
            canvas.create_text(x - vertical_space / 2, window_height - con.DOWN_SPACE // 2 , text=f"{j}", anchor="n", font=("Arial", 10), fill="black")

    # Rysowanie wybranyh dźwięków
    pos = sounds.isolate_notes(tuning_button.get(), scale_button.get(), tonation_button.get(), sounds_position())
    for note, x, y in pos:
            r = horizontal_space / 2
            canvas.create_oval(x-r, y-r, x+r, y+r, fill="lightblue", outline="black", width=0)
            #Wypisywanie wybranych dźwięków
            if notes_visibility_value.get():  
                canvas.create_text(x, y, text=note, font=("Arial", int(r), "bold"), fill="darkblue")



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



# --- Tworzenie głównego okna ---
window = tk.Tk()
window.title("Siatka linii reagująca na rozmiar okna")
window.geometry("1000x400")

#==========================================================
#======  comboboxy  =======================================
#==========================================================

combobox_frame = tk.Frame(window)
combobox_frame.pack(side="top", anchor="nw", padx=10, pady=10)

# --- combobox ze strojeniami ---

tuning_button = ttk.Combobox(combobox_frame, values=list(con.TUNINGS.keys()), state="readonly")
tuning_button.set("STANDARD")  
tuning_button.pack(pady=5, padx=10, side="left")
tuning_button.bind("<<ComboboxSelected>>", draw_fretboard)

# --- combobox ze skalami ---

scale_button = ttk.Combobox(combobox_frame, values=list(con.SCALES.keys()), state="readonly")
scale_button.set("PENTATONIC")  
scale_button.pack(pady=5, padx=10, side="left")
scale_button.bind("<<ComboboxSelected>>", draw_fretboard)


# --- combobox z tonacjami ---

tonation_button = ttk.Combobox(combobox_frame, values=sorted(con.TONATIONS), state="readonly")
tonation_button.set("C")  
tonation_button.pack(pady=5, padx=10, side="left")
tonation_button.bind("<<ComboboxSelected>>", draw_fretboard)



combobox_frame = tk.Frame(window)
combobox_frame.pack(side="top", anchor="nw", padx=10, pady=10)


# --- checkbox "czy wyświetlać nazwy dźwięków" --- 

notes_visibility_value = tk.BooleanVar(value=True)  # Domyślnie zaznaczony
notes_visibility_checkbox = tk.Checkbutton(combobox_frame, text="Pokaż dźwięki", variable=notes_visibility_value, command=draw_fretboard)
notes_visibility_checkbox.pack(pady=0, padx=10, side="left")


# --- Tworzenie canvasu ---
canvas = tk.Canvas(window, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# --- Automatyczne rysowanie przy zmianie rozmiaru okna ---
window.bind("<Configure>", draw_fretboard)

# --- Pierwsze rysowanie ---
def start():
    draw_fretboard()
    window.mainloop()

