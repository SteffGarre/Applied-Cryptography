import operator

try:
    ciphertext = open("cipher2.txt", "r")
except:
    print("Error reading file, check input!")
    exit()

#Remove newlines from file    
ciphertext = ciphertext.read().replace('\n', '')
lst = {}

# Go through every char and count occurrences.
for char in ciphertext:
    if char in lst:
        lst[char] = lst[char] + 1
        continue
    lst[char] = 1

print()
print("Nr of unique symbols:", len(lst))
print(dict(sorted(lst.items(), key=operator.itemgetter(1),reverse=True)))
