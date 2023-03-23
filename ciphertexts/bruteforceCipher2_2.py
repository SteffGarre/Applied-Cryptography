# define first line of ciphertext2 and corresponding used alphabet
orig_string = "_PE4UJ8ZODIPA#QG4VK9_PU#MB0SG5WLA#4BYNTPKCJ03T4CGMMNO5J072QC88AHC#GQ00"
symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_#"

# give every symbol in alphabet a corresponding value: 0,1,...,n
# and store results in char_to_val_list, val_to_char_list is the
# reversed key-val pair
char_to_val_list = {}
val_to_char_list = {}
counter = 0
for char in symbols:
    char_to_val_list[char] = counter
    val_to_char_list[counter] = char
    counter += 1

counter = 0
start = 0
current = 0
# The nested for loops go through each combination for key length = 4
# Assuming the actual key length is longer, each key lenght > 4 is
# handled by printing a ".", the output is then manually analysed
for k1 in range(start,38):
    for k2 in range(0,38): 
        for k3 in range(0,38):
            for k4 in range(0,38):
                
                # The different keys alternate based on key length
                for char in orig_string:
                    # reset counter
                    if counter == 9:
                        counter = 0
                        
                    # Go trough different printing options
                    if counter == 0:
                        current = k1
                    if counter == 1:
                        current = k2
                    if counter == 2: 
                        current = k3
                    if counter == 3: 
                        current = k4
                    if counter > 3 and counter < 9:
                        print(".", end='')
                        counter +=1
                        continue
                        
                    pos = (char_to_val_list[char]+current)%38
                    print(val_to_char_list[pos], end='')
                    counter += 1
                counter = 0
                print() 
    
