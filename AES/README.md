# AES 128 bit encryption 
AES encryption implemented for the course Applied Cryptography – DD2520

## Quick rundown of the code implemented
1. Main
..* Read 16 bytes from stdin (the first 16 bytes contains the cipher key for AES.)
..* Expand the cipher key with the key_expansion_128bit function and return a list of lists containing 44 lists representing 11 4x4 matrices that contains the round keys for AES.
..* Read 16 bytes from stdin and send the bytes with the round keys to the encrypt_128bit function to encrypt according to AES. Repeat until no more bytes left of plaintext.
