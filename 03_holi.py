"""
This function checks a grid (like a 2D map of emojis) to see 
which colors from the master list are missing!
    
How the magic happens:
1. We start with a full list of all possible rainbow colors.
2. We use a 'set' to collect every color actually inside the grid.
3. We loop through the master list and ask: "Is this color here?"
4. If the answer is "No," we add that color to our missing list!
    
It’s a super efficient way to find the 'voids' in your rainbow.
"""

def find_missing_colors(grid):
    # Write code below 💖
    all_colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
    
    present_colors = set()
    for row in grid:
        for color in row:
            present_colors.add(color)
            
    missing = []
    for color in all_colors:
        if color not in present_colors:
            missing.append(color)
            
    return missing
