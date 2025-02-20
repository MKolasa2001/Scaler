#parametry gryfu
STRINGS_NUMBER = 6
FRETS_NUMBER = 21
RATIO = 2.0       # Height to width ratio in fret

LEFT_SPACE = 50
RIGHT_SPACE = 25
DOWN_SPACE = 30

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

TONATIONS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
             "Cm", "C#m", "Dm", "D#m", "Em", "Fm", "F#m", "Gm", "G#m", "Am", "A#m", "Bm"]

TUNINGS = {
    "STANDARD": ["E", "B", "G", "D", "A", "E"],
    "DROP D": ["E", "B", "G", "D", "A", "D"]
}

SCALES = {
"PENTATONIC":   [[0, 2, 4, 5, 7, 9, 11], [0, 2, 3, 5, 7, 8, 10]],
"BLUES":        [[0, 2, 3, 4, 7, 9],     [0, 3, 5, 6, 7, 10]]
}