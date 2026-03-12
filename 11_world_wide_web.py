"""
This function verifies if a web address follows the basic 
rules of the internet. 
    
The Security Check:
1. Protocol Check: It ensures the address starts with either 
   'http://' or 'https://'.
2. Domain Check: It splits the string to find the domain and 
   makes sure there is at least one '.' present.
3. Character Cleanliness: It loops through the domain to 
   ensure every character is either a letter, a number, 
   a hyphen, or a dot.
"""
def check_url(address):
    # Write code below 💖
    if not (address.startswith("http://") or address.startswith("https://")):
        return "invalid"
  
    domain = address.split("://")[1]
  
    if "." not in domain:
        return "invalid"
  
    for char in domain:
        if not (char.isalnum() or char in "-."):
            return "invalid"
            
    return "valid"
