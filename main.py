import tkinter as tk
from tkinter import ttk
import constants as con
import sounds

def dwar_fretboard(event=None):
    canvas.delete("all")  # Wyczyść poprzednie linie

    szerokosc = canvas.winfo_width()
    window_height = canvas.winfo_height()

    pos = sounds.isolate_notes("STANDARD", "PENTATONIC", "C", sounds_position())
    for note, x, y in pos:
            r = 5
            canvas.create_oval(x-r, y-r, x+r, y+r, fill="lightblue", outline="black", width=0)


    canvas.create_text(10, 10, text="Siatka linii", anchor="nw", font=("Arial", 16, "bold"), fill="blue")

    # Oblicz odstępy
    odstęp_pionowy = (szerokosc - con.LEFT_SPACE - con.RIGHT_SPACE) / (con.FRETS_NUMBER - 1)
    odstęp_poziomy = odstęp_pionowy / con.RATIO
    

    # Rysuj poziome linie
    for i in range(con.STRINGS_NUMBER):
        y = window_height - con.DOWN_SPACE - i * odstęp_poziomy 
        canvas.create_line(con.LEFT_SPACE, y, szerokosc - con.RIGHT_SPACE, y, width=2, fill="black")

    # Rysuj pionowe linie (ograniczone do obszaru poziomych linii)
    for j in range(con.FRETS_NUMBER):
        x = j * odstęp_pionowy + con.LEFT_SPACE
        grubość = 4 if j == 0 else 1  # Pierwsza pionowa linia grubsza

        fret_start = window_height - con.DOWN_SPACE - (con.STRINGS_NUMBER - 1) * odstęp_poziomy
        canvas.create_line(x, fret_start, x, window_height - con.DOWN_SPACE , width=grubość, fill="black")
        if j != 0:
            canvas.create_text(x - odstęp_pionowy / 2, window_height - con.DOWN_SPACE , text=f"{j}", anchor="n", font=("Arial", 10), fill="black")

def sounds_position():
    szerokosc = canvas.winfo_width()
    window_height = canvas.winfo_height()

    odstęp_pionowy = (szerokosc - con.LEFT_SPACE - con.RIGHT_SPACE) / (con.FRETS_NUMBER - 1)
    odstęp_poziomy = odstęp_pionowy / con.RATIO

    positions = {}

    for i in range(con.STRINGS_NUMBER):
        positions[window_height - con.DOWN_SPACE - i * odstęp_poziomy] = [] 

    # Rysuj pionowe linie (ograniczone do obszaru poziomych linii)
    for j in range(con.FRETS_NUMBER):
        x = j * odstęp_pionowy + con.LEFT_SPACE
        for pos in positions.values():
            pos.append(int(x - odstęp_pionowy / 2))
    return positions

def zmien_kolor(event):
    dwar_fretboard()

# --- Tworzenie głównego okna ---
okno = tk.Tk()
okno.title("Siatka linii reagująca na rozmiar okna")
okno.geometry("800x400")

# --- Rozwijana lista (kolory) ---
kolory = ["black", "red", "blue", "green", "orange", "purple"]
wybor_koloru = ttk.Combobox(okno, values=kolory, state="readonly")
wybor_koloru.set("black")  # Domyślny kolor
wybor_koloru.pack(pady=10)
wybor_koloru.bind("<<ComboboxSelected>>", zmien_kolor)


# --- Tworzenie canvasu ---
canvas = tk.Canvas(okno, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# --- Automatyczne rysowanie przy zmianie rozmiaru okna ---
okno.bind("<Configure>", dwar_fretboard)

# --- Pierwsze rysowanie ---
dwar_fretboard()

okno.mainloop()

