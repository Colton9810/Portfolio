# my imports, I imported the string library to make it easier to add the alphabet to my list without typing it out

from sys import stdin, argv
import string

# creating my alphabet list
ALPHABET = list(string.ascii_uppercase)
ALPHABET += string.ascii_lowercase

# here is the function that will encrypt the given text with the given key
def encrypt(plaintext, key):
    ciphertext = ""

    # i used two separate variable for the indexes of the key and text
    # did this so that i would be able to reset the index for key when it reached the end of it
    i = 0
    j = 0

    # a loop that will only break when the entirety of the text is looked at
    while True:
        # the first case when i & j are both in the range of the text and key
        if (j <= len(plaintext) - 1 and i <= len(key) - 1):
            # checks if our char is in the index for both the key and text
            if (plaintext[j] not in ALPHABET or key[i] not in ALPHABET):
                # if the text isn't in our list than add that char to the final string, then increase the index of the text
                if (plaintext[j] not in ALPHABET):
                    ciphertext += plaintext[j]
                    j += 1
                # if it is the key that is out of the list than increase the index of the key
                else:
                    i += 1
            # if the code reaches here both the key and text were in the list
            else:
                # finds the character index associated with the key[index]
                for k in range(len(ALPHABET)):
                    if (key[i] == ALPHABET[k]):
                        keyValue = k
                        break
                # finds the character index associated with the text[index]
                for l in range(len(ALPHABET)):
                    if (plaintext[j] == ALPHABET[l]):
                        plaintextValue = l
                        break
                # i dealt with lowercase letters by first converting them to uppercase, running the formula, the converting back to lowercase
                # i put all of the lowercase letters at the end of the list so it was easy to determine the case of each specific char by the index
                if (plaintextValue >= 26):
                    cipherKey = (keyValue + (plaintextValue - 26)) % 26
                    ciphertext += ALPHABET[cipherKey + 26]
                    i += 1
                    j += 1
                else:
                    cipherKey = (keyValue + plaintextValue) % 26
                    ciphertext += ALPHABET[cipherKey]
                    i += 1
                    j += 1
        # case #2 where j is out of the range of the text, this is where we break the big loop
        elif (j > len(plaintext) - 1):
            break
        # the third case is where we get to the end of the key
        # this will reset the index of the key to 0 so that we will restart from the beginning of it
        else:
            i = 0
    # returns the string that we have been building in this function
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""

    # i used two separate variable for the indexes of the key and text
    # did this so that i would be able to reset the index for key when it reached the end of it
    i = 0
    j = 0

    # a loop that will only break when the entirety of the text is looked at
    while True:
        # the first case when i & j are both in the range of the text and key
        if (j <= len(ciphertext) - 1 and i <= len(key) - 1):
            # checks if our char is in the index for both the key and text
            if (ciphertext[j] not in ALPHABET or key[i] not in ALPHABET):
                # if the text isn't in our list than add that char to the final string, then increase the index of the text
                if (ciphertext[j] not in ALPHABET):
                    plaintext += ciphertext[j]
                    j += 1
                # if it is the key that is out of the list than increase the index of the key
                else:
                    i += 1
            # if the code reaches here both the key and text were in the list
            else:
                # finds the character index associated with the key[index]
                for k in range(len(ALPHABET)):
                    if (key[i] == ALPHABET[k]):
                        keyValue = k
                        break
                # finds the character index associated with the text[index]
                for l in range(len(ALPHABET)):
                    if (ciphertext[j] == ALPHABET[l]):
                        ciphertextValue = l
                        break
                # i dealt with lowercase letters by first converting them to uppercase, running the formula, the converting back to lowercase
                # i put all of the lowercase letters at the end of the list so it was easy to determine the case of each specific char by the index
                if (ciphertextValue >= 26):
                    cipherKey = (ciphertextValue - keyValue) % 26
                    plaintext += ALPHABET[cipherKey + 26]
                    i += 1
                    j += 1
                else:
                    cipherKey = (26 + ciphertextValue - keyValue) % 26
                    plaintext += ALPHABET[cipherKey]
                    i += 1
                    j += 1
        # case #2 where j is out of the range of the text, this is where we break the big loop
        elif (j > len(ciphertext) - 1):
            break
        # the third case is where we get to the end of the key
        # this will reset the index of the key to 0 so that we will restart from the beginning of it
        else:
            i = 0

    # returns the string that we have been building in this function
    return plaintext

# takes the first argument and makes it the mode, second argument becomes the key
mode = "-d"#argv[1]
key = "vigenere"#argv[2]

# gets the text from standard input
text = "Bw hepo ks opk frkzriqtk bj klda ilnpciiok avxy y:kmvtrv g:vzxvic.  Xyii okx glv hzuurf slx."    #stdin.read().rstrip("\n")

# if the first argument is to encrypt
if (mode == "-e"):
    ciphertext = encrypt(text, key)
    print(ciphertext)
# if the first argument is to decrypt
elif (mode == "-d"):
    plaintext = decrypt(text, key)
    print(plaintext)