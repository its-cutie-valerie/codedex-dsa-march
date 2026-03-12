"""    
This function calculates a skater's total technical score 
by processing each element (like jumps or spins).
  
The Step-by-Step:
1. We look at each element's name, base value, and a list 
   of GOE (Grade of Execution) scores from the judges.
2. We sort the judges' scores and 'trim' them—dropping the 
   highest and lowest scores to avoid any bias!
3. We find the average of the remaining middle scores.
4. The final score for that move is the base value plus 
   a percentage bonus based on that average.
5. Finally, we sum everything up and round it to 1 decimal!
"""
def calculate_score(elements):
    # Write code below 💖
    total_tes = 0
    for name, base_value, goes in elements:
        sorted_goes = sorted(goes)
        trimmed_goes = sorted_goes[1:-1]
        avg_goe = sum(trimmed_goes) / len(trimmed_goes)
        
        element_score = base_value + (avg_goe * 0.1 * base_value)
        total_tes += element_score
        
    return round(total_tes, 1)
