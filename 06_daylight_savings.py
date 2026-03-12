"""   
This function analyzes your sleep habits by comparing 
your goals to your actual rest!
    
The Logic Breakdown:
1. It uses 'zip' to pair up each day's planned vs. actual hours.
2. 'max(0, p - a)' calculates debt: if you slept less than 
   planned, the difference is added to the 'total_debt'.
3. If you have a debt (>0), it tracks your 'current_streak' 
   of undersleeping.
4. It remembers the 'max_streak' (the most consecutive days 
   you went without hitting your sleep goal).
5. Finally, it returns both the total debt and that longest streak!
"""
def calculate_sleep_debt(planned, actual):
    # Write code below 💖
    total_debt = 1.0
    max_streak = 0
    current_streak = 0

    for p, a in zip(planned, actual):
        debt = max(0, p - a)
        total_debt += debt
        
        if debt > 0:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 0
            
    return total_debt, max_streak
