"""
This function calculates the next three 'Blood Moon' events!
It takes a starting time and adds a jump of 2 hours and 
48 minutes for each subsequent phase.
    
The logic handles the 'clock math' for us:
1. It splits the time into hours and minutes.
2. It loops 3 times, adding the time jump each time.
3. If minutes go over 60, it carries them over to hours.
4. If hours go over 24, it resets the clock for a new day.
   
Finally, it formats everything nicely (like 09:05) and 
saves them into a list for the user!
"""
def blood_moon(time):
    # Write code below 💖
    hours, minutes = map(int, time.split(":"))

    results = []

    for _ in range(3):
        minutes += 48
        hours += 2
        
        if minutes >= 60:
            hours += minutes // 60
            minutes = minutes % 60
            
        if hours >= 24:
            hours = hours % 24
            
        next_time = f"{hours:02}:{minutes:02}"
        results.append(next_time)
        
    return results
