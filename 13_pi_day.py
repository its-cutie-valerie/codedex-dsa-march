"""
This function calculates the length of the crust for 
each slice of pie so everyone gets a fair share!
    
The Steps:
1. It uses 'pi' to calculate the total circumference 
   (the crust) based on the diameter provided.
2. It divides that total crust length by the number 
   of friends.
3. It rounds the result to two decimal places so 
   you have a clean measurement for your knife!
"""
# Write code below 💖
from math import pi
def cut_pie(diameter, friends):
    pie = pi * diameter
    slices = pie / friends
    return round(slices, 2)
