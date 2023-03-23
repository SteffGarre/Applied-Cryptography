def get_corresp_char(char):
    ascii_val = ord(char)
    
    #Special case for 0, # and _ 
    if ascii_val == 48:
        return "\n"
    if ascii_val == 35:
        return " "
    if ascii_val == 95:
        return "Z"
    
    # For all other chars move 1 step to the left
    ascii_val = ascii_val - 1
    return chr(ascii_val)

try:
    ciphertext = open("cipher1.txt", "r")
except:
    print("Error reading file, check input!")
    exit()

#Remove newlines from file    
ciphertext = ciphertext.read().replace('\n', '')

#Go through every character: decrypt and print
for c in ciphertext:
    print(get_corresp_char(c), end = '')

print()
print("*** Decryption finished ***")