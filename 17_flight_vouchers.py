"""
This function finds the most efficient voucher to use 
by calculating a 'value-to-wait' ratio!
    
The Logic:
1. Filter: It first checks the 'delays' list to make sure 
   the wait time is within your 'max_wait' limit.
2. The Ratio: For every valid voucher, it divides the 
   voucher value by its delay (Value / Time).
3. The Winner: It keeps track of the 'max_ratio' found 
   so far. If a new voucher has a higher ratio, it 
   becomes the new top choice.
4. Result: It returns the index of the best voucher so 
   you know exactly which one to grab!
"""
def pick_voucher(vouchers, delays, max_wait):
    # Write code below 💖
    best_index = -1
    max_ratio = -1.0
  
    for i in range(len(vouchers)):
        if delays[i] <= max_wait:
            ratio = vouchers[i] / delays[i]
      
            if ratio > max_ratio:
                max_ratio = ratio
                best_index = i
        
    return best_index
