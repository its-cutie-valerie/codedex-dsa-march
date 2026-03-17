"""    
This function predicts how "luck" (☘️) spreads down a 
river as time goes by!
    
The Logic:
1. It starts by making a copy of the original river so 
   it doesn't accidentally change the starting point 
   while it's still calculating.
2. It loops through every spot in the river. 
3. When it finds a clover (☘️), it looks at the 'hours' 
   given and spreads that luck to the next 'h' spots 
   downstream.
4. It carefully checks that it doesn't go past the end 
   of the river (the 'len' check).
       
The result is a river where the luck has drifted forward!
"""
def lucky_river(river, hours):
    # Write code below 💖
    new_river = list(river)
    for i in range(len(river)):
        if river[i] == '☘️':
            for h in range(1, hours + 1):
                if i + h < len(river):
                    new_river[i + h] = '☘️'
    return new_river
