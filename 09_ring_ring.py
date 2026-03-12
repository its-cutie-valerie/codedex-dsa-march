"""    
This function cleans up a transcript and counts every 
individual word—but only once!
    
The Cleaning Process:
1. It loops through every character to remove punctuation. 
   Only letters, numbers, and spaces are allowed to stay!
2. It converts everything to lowercase so "Hello" and 
   "hello" aren't counted as different words.
3. It 'splits' the clean text into a list of words.
4. It uses a 'set' to instantly delete all duplicates, 
   leaving only the unique vocabulary behind!
"""
def find_unique_words(transcript):
    # Write code below 💖    
    cleaned = ''
    
    for char in transcript:
        if char.isalnum() or char.isspace():
            cleaned += char.lower()
    
    words = cleaned.split()
    
    return len(set(words))
