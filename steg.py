##########################
## Name: Jimmie Gann    ##
## Class: CSC 442       ##
## Date: 5/7/2020       ##
## Version: Python v3.8 ##
##########################
from sys import stdout, argv

# The constant sentinel variable so can easily be changed here
sentinel = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
SENTINEL = bytearray(sentinel)

# The constant that stores what the file is saved as
# IF THE MAIN FILE NAME IS CHANGED MUST CHANGE THIS VARIABLE FOR MY LOGIC TO WORK
file_name = 'steg.py'

# sudo code in notes, goes over this around the 1 hr mark in the video
method = ''
mode = ''
offset = 0
interval = 1
wrapper = ''
hidden = ''

# This loop will cycle through all the terminal arguments and saves them into to the variable for those arguments
# It is set up so that no matter the order they are received they will be put into the correct variables
for i in argv:
    if i == file_name:
        pass
    elif i[1] == 's' or i[1] == 'r':
        method = i[1]
    elif i[1] == 'b' or i[1] == 'B':
        mode = i[1]
    elif i[1] == 'o':
        offset = int(i[2:])
    elif i[1] == 'i':
        interval = int(i[2:])
    elif i[1] == 'w':
        wrapper = i[2:]
    elif i[1] == 'h':
        hidden = i[2:]
    # If given an invalid argument, send an error message and exit the program
    else:
        stdout.write("One or more invalid commands, please enter ' -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]' as your commands\n")
        exit()

# If any of the required arguments are missing give an error message and exit the program
if method == '' or mode == '' or wrapper == '':
    stdout.write("One or more incomplete commands, -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]' as your commands. Method, mode, and wrapper file is required!\n")
    exit()

# Right here I open the files and get them into bytearrays
W = open(wrapper, 'rb')
W = bytearray(W.read())


if mode == 'B':
    if method == 's':

        # I do this so we don't get an error when no hidden file is given
        if hidden != '':
            H = open(hidden, 'rb')
            H = bytearray(H.read())
        else:
            stdout.write("You are not able to run the store command without a hidden file to import")
            exit()

        # Adds sentinel to the end of the hidden file
        SENTINEL[0:0] = H

        # I copy the offset variable here so i can use it again later
        i = 0
        offset2 = offset

        while i < len(H):
            W[offset2] = H[i]
            offset2 += interval
            i += 1

        i = 0

        while i < len(SENTINEL):
            W[offset] = SENTINEL[i]
            offset += interval
            i += 1

    # Else run the extraction code
    else:
        i = 0
        length = int((len(W) - offset) / interval)
        H = bytearray(length + 1)

        while i < len(W):
            b = W[offset]

            if H[i - 6:i] == SENTINEL:
                H = H[:i - 6]
                break
            else:
                H[i] = b
                offset += interval
                i += 1

        stdout.buffer.write(H)

elif mode == 'b':
    if method == 's':
        # I do this so we don't get an error when no hidden file is given
        if hidden != '':
            H = open(hidden, 'rb')
            H = bytearray(H.read())
        else:
            stdout.write("You are not able to run the store command without a hidden file to import")
            exit()
        # Adds sentinel to the end of the hidden file
        SENTINEL[0:0] = H
        i = 0

        while i < len(H):
            for j in range(8):
                W[offset] &= 0b11111110
                W[offset] |= ((H[i] & 0b10000000) >> 7)
                H[i] << 1 & ((2 ** 8) - 1)
                offset += interval
            i += 1
        i = 0

        while i < len(SENTINEL):
            for j in range(8):
                W[offset] &= 0b11111110
                W[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
                SENTINEL[i] << 1 & ((2 ** 8) - 1)
                offset += interval
            i += 1

    else:
        i = 0
        H = bytearray(len(W))

        while offset < len(W):
            b = 0

            for j in range(8):
                b |= (W[offset] & 0b00000001)

                if j < 7:
                    b <<= 1 & (2 ** 8 - 1)
                    offset += interval

            if H[i - 6:i] == SENTINEL:
                H = H[:i - 6]
                break
            else:
                H[i] = b
                offset += interval
                i += 1

        stdout.buffer.write(H)
