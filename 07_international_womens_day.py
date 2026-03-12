"""    
This function performs a deep dive into a list of percentages 
to figure out the "big picture" of the data.
    
The Triple-Check:
1. Net Change: It calculates the average change per step from 
   the very first entry to the very last.
2. The Trend: It compares the average of the FIRST three 
   points to the LAST three points to see if the overall 
   vibe is "improving," "stagnating," or "declining."
3. The Dips: It counts every single time a number was lower 
   than the one before it—identifying any rough patches.
    
It returns all three insights in one neat package!
"""
def analyze(percentages):
    # Write code below 💖

    net = round((percentages[-1] - percentages[0]) / (len(percentages) - 1), 5)

    first_three = sum(percentages[:3]) / 3
    last_three = sum(percentages[-3:]) / 3

    if last_three > first_three:
        trend = "improving"
    elif last_three == first_three:
        trend = "stagnating"
    else:
        trend = "declining"

    dips = 0
    for i in range(1, len(percentages)):
        if percentages[i] < percentages[i-1]:
            dips += 1

    return net, trend, dips
