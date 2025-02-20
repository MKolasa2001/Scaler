import constants as con

def shift_note(note, interval):
    return con.NOTES[(con.NOTES.index(note) + interval) % 12]

def generate_notes(scale, tonation):
    is_minor = 0
    if tonation.endswith("m"):
        is_minor = 1
        tonation = tonation[:-1]

    tonation_shift = con.NOTES.index(tonation)
    intervals = [(x + tonation_shift) % 12 for x in con.SCALES[scale][is_minor]]
    return [con.NOTES[i] for i in intervals]
    

def isolate_notes(tuning, scale, tonation, positions):
    notes = generate_notes(scale, tonation)
    notes_pos = []

    for y, sound in list(zip(sorted(positions.keys()), con.TUNINGS[tuning])):
        for x in positions[y]:
            note = shift_note(sound, positions[y].index(x))
            if note in notes:
                notes_pos.append([note, x, y])
    return notes_pos
            

    
    



#generate_notes("STANDARD", "PENTATONIC", "C")