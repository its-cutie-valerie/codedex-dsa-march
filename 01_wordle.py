"""    
This function acts as the judge for a 5-letter word game!
It loops through every letter (0 to 4) and checks if the 
player's guess has the exact same letter in the exact 
same spot as the secret word.    
If they match perfectly, we add 1 to our count!
"""

def wordle_guess(secret, guess):
  # Write code below 💖
  count = 0

  for i in range(5):
    if secret[i] == guess[i]:
      count += 1
  return count
