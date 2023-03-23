symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_#"

try:
    ciphertext = open("cipher2.txt", "r")
except:
    print("Error reading file, check input!")
    exit()
    
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

#Remove newlines from file    
ciphertext = ciphertext.read().replace('\n', '')

#key for decryption
key = [2,14,26,37,12,24,36,10,22,34,30,24]
current = 0

#Go through every character: decrypt and print
for char in ciphertext:
    
    if current == 12:
        current = 0
        
    pos = (char_to_val_list[char]+ key[current])%38
    
    if val_to_char_list[pos] == '_':
        print(' ', end='')
        current += 1
        continue
    
    if val_to_char_list[pos] == '#':
        print('\n', end='')
        current += 1
        continue

    print(val_to_char_list[pos], end='')
    current += 1   
print()
print("*** Decryption finished ***")