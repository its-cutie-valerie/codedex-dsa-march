"""    
This function calculates the total minutes needed to reach 
the ground from a specific altitude. 
(like, when a certain kitty went up there)
    
How the calculation works:
1. It defines five different atmospheric 'spheres,' each with 
   its own descent rate (dr). 
2. Higher altitudes usually have faster descent rates, while 
   lower ones are slower (like passing through thicker air).
3. It loops through each layer: if the current altitude is 
   within that layer, it calculates the distance traveled 
   and divides it by that layer's specific rate.
4. It adds up the time from every layer passed and rounds 
   it to one decimal place for a clean final reading!
"""
def calculate_descent(altitude):
    # Write code below 💖
    if altitude == 0:
        return 0.0  

    spheres = [
        {"lower": 700, "upper": 10000, "dr": 2000},
        {"lower": 85, "upper": 700, "dr": 500},
        {"lower": 50, "upper": 85, "dr": 200},
        {"lower": 12, "upper": 50, "dr": 75},
        {"lower": 0, "upper": 12, "dr": 20},
    ]

    total = 0

    for sphere in spheres:
        lower = sphere["lower"]
        upper = sphere["upper"]
        dr = sphere["dr"]

        if altitude > lower:
            min_val = min(altitude, upper) - lower  
            total += (min_val * 1000) / dr  

    return round(total, 1)
