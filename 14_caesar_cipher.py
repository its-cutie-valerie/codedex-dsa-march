"""    
This function cracks a Caesar Cipher by shifting letters 
backward to reveal a hidden message!
    
The Steps:
1. The Shift: It uses 'shift % 26' to make sure the shift 
   stays within the alphabet (even if the number is huge!).
2. The Space Rule: It ignores spaces so the sentence 
   structure stays the same.
3. The ASCII Math: It converts each letter to its number 
   code (ord), subtracts the shift, and turns it back into 
   a letter (chr).
4. The Loop-around: If the shift goes "past a," it adds 26 
   to wrap back around to the end of the alphabet.
"""
def decode_message(message, shift):
    # Write code below 💖
    shift = shift % 26

    decoded = ""

    for char in message:
      if char == " ":
        decoded += " "
      else:
        shifted_char = ord(char) - shift

        if shifted_char < ord('a'):
          shifted_char += 26

        decoded += chr(shifted_char)
    return decoded
