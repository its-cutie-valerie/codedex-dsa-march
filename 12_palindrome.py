"""    
This function checks if a word or phrase is a perfect 
palindrome (like "Racecar" or "Never odd or even").
    
The Logic:
1. Normalization: It removes all spaces and converts the 
   text to lowercase so the check isn't picky.
2. The Flip: It uses the slice trick [::-1] to create a 
   perfectly reversed version of the string.
3. The Comparison: It compares the clean version to the 
   reversed version. If they match, it's a palindrome! Yippee!
"""

def check_palindrome(sequence):
    # Write code below 💖
    worky_sequence = sequence.replace(" ", "").lower()
    return worky_sequence == worky_sequence[::-1]
