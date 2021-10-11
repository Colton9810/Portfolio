import socket
from sys import stdout
from time import time

# enables debugging output
DEBUG = False

# I use this to check if we got 'EOF' and broke out of the loop,
# then use this to print the string without printing 'EOF
broke = False

# This is where the variable for the timing of a '1' can be changed
ONE = .2

# set the server's IP address and port
ip = "138.47.102.67"
port = 33333

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096)
bin_str = ''
text = ''

while (data.rstrip("\n") != "EOF"):
    # output the data
    stdout.write(data)
    stdout.flush()
    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)

    if delta >= ONE:
        bin_str += "1"
    else:
        bin_str += "0"

    if (DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

while bin_str != "":
    char = bin_str[:8]
    char = int(char, 2)

    if text[-3:] == "EOF":
        broke = True
        break
    elif (char == 8):
        # remove the last character that was added to our text
        text = text[:-1]
    else:
        # adds any other character to our text
        text += chr(char)

    bin_str = bin_str[8:]

# close the connection to the server
s.close()

# Print out the final results
if broke:
    stdout.write(text[:-3] + "\n")
else:
    stdout.write(text + "\n")
