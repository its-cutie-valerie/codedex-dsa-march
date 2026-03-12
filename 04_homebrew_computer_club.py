"""
This function converts binary switch signals into 
musical notes! Think of it as a bridge between 
raw computer data and a melody.
   
The process:
1. We define a 'note_map' dictionary that links 
   specific numbers (frequencies) to their note 
   names (like C4, D4, etc.).
2. We loop through each 'binary_string' in the 
   switches list.
3. 'int(binary_string, 2)' converts those 0s and 1s 
   into a regular decimal number.
4. We look up that number in our map and add the 
   corresponding note to our song!
"""
def dompier_music(switches):
    # Write code below 💖
    note_map = {
        261: "C4",
        294: "D4",
        329: "E4",
        349: "F4",
        392: "G4",
        440: "A4",
        494: "B4",
        523: "C5",
        0: "REST"
    }
    
    song = []
    for binary_string in switches:
        decimal_val = int(binary_string, 2)
        note = note_map.get(decimal_val)
        song.append(note)
        
    return song
