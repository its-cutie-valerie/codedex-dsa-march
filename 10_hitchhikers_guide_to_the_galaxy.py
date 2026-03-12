"""
This function searches for the smallest combination of 
numbers that sums up to exactly 42.
    
How it works:
1. It starts with a size of 1 and goes up to the full 
   length of the list.
2. Using 'combinations', it checks every possible group 
   of numbers for that specific size.
3. The moment it finds a group that sums to 42, it stops 
   and returns that size (since we started small, we 
   know it's the minimum!).
4. If it checks every possible combo and finds nothing, 
   it returns -1.
"""
from itertools import combinations
def minimum_components(components):
    # Write code below 💖
    number_of_meaning_of_life = 42
    
    for n in range(1, len(components) + 1):
        for comb in combinations(components, n):
            if sum(comb) == number_of_meaning_of_life:
                return n
                
    return -1
