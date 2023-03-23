import operator

try:
    ciphertext = open("cipher1.txt", "r")
except:
    print("Error reading file, check input!")
    exit()

#Remove newlines from file    
ciphertext = ciphertext.read().replace('\n', '')
#Split at character = # 
cipher_splitted = ciphertext.split("#")
lst = {}

# Go through every word after splitting at # and count occurrences.
for word in cipher_splitted:
    if word == "":
        continue
    if word in lst:
        lst[word] = lst[word] + 1
        continue
    lst[word] = 1

print()
print("Nr of unique words:", len(lst))
print(dict(sorted(lst.items(), key=operator.itemgetter(1),reverse=True)))
    