import socket
from time import sleep
from binascii import hexlify

# set the port for client connections
port = 1337

# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))

# listen for clients
# this is a blocking call
s.listen(0)

# a client has connected!
c, addr = s.accept()

# set the message
msg = "Some sort of overt message is being transmitted here. But there is a hidden message being covertly transmitted! Can you guess it? \n"
covert = "Covert message: Gourd is 31337! Of course, we already knew this..." + "EOF"
covert_bin = ''

for i in covert:
	covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)

ZERO = 0.025
ONE = 0.1
# send the message, one letter at a time
n = 0

for i in msg:
	c.send(i)

	if (covert_bin[n] == "0"):
		sleep(ZERO)
	else:
		sleep(ONE)

	n = (n + 1) % len(covert_bin)

# send EOF and close the connection to the client
c.send("EOF")
c.close()

