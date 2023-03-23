# AES 128-bit encryption 
AES encryption implemented for the course Applied Cryptography – DD2520

## Quick rundown of the code implemented

**1. Main**
* Read 16 bytes from stdin (the first 16 bytes contains the cipher key for AES.)
* Expand the cipher key with the key_expansion_128bit function and return a list of lists containing 44 lists representing 11 4x4 matrices that contains the round keys for AES.
* Read 16 bytes from stdin and send the bytes with the round keys to the encrypt_128bit function to encrypt according to AES. Repeat until no more bytes left of plaintext.

**2. Key expansion**
 
* The key_expansion_128bit function receives 16 raw bytes representing the secret key.
* The function returns keys, a list of lists. 
* Each list contains 4 elements. Every element is an integer representing a byte (0-255).
* 4 consecutive lists give us a 4x4 matrix representation of 16 bytes. In total, keys contain 44 lists, representing 11 matrices (the roundkeys according to AES 128 bit).

*Algorithm:*
  * Store the initial cipher key without modification in keys.
  * for i in range (0,40):
    * Grab the current last list in keys.
    * Whenever we begin with a new round key, modify the last list (the last 4 bytes of the 4x4 matrix) according to AES:
      * Do RotWord()
      * Do SubWord()
      * Do Rcon
    * xor the last list with the current i list
   
When the loop is completed, keys should have 44 lists, the first 4 represents the original cipher key, the next 40 the derived round keys.
return the list keys.

**3. Encryption**

* The encrypt_128bit function takes plaintext (16 raw bytes) and the list keys containing the round keys.
* The function creates a list state that contains 4 lists (a 4x4 matrix) , representing the current state of the plaintext as it is modified during the different “encryption stages”.
* The encrypt_128bit function calls the following functions in order to modify the list state (according to AES):
 * addRoundKey(): XOR the current state with a corresponding round key.
 * subBytes(): Substitute every byte in state by using the predefined sub_box.
 * shiftRows(): Shift rows in state accor. to an offset. No shift is done on row 0.
 * mixColumns(): Matrix multiplication using GF arithmetics.

*Algorithm:*
* Store the initial plaintext (16 bytes) in the list state.
* Do the initial round: call addRoundKey(state, round key 0)
* Since we implement the 128 bit encryption of AES, we do 10 rounds.
* for i in range (1,10):
  * subBytes(state)
  * shiftRows(state)
  * mixColumns(state)
  * addRoundKeys(state, round key i)
* Do the final round: 
  * subBytes(state)
  * shiftRows(state)
  * addRoundKeys(state, round key 10)
* Write state to stdout to print the encrypted 16 bytes of plaintext


