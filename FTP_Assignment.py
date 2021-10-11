##########################
## Name: Jimmie Gann    ##
## Class: CSC 442       ##
## Date: 4/3/2020       ##
## Version: Python v2.7 ##
##########################

# Import necessary libraries
from ftplib import FTP

# Site specifics / specific variables
IP = "jeangourd.com"
PORT = 8008
USER = "valkyrie"
PASSWORD = "chooseroftheslain"
USE_PASSIVE = True
FOLDER = "/.secretstorage/.folder2/.howaboutonemore"

METHOD = 10
contents1 = []

# Using ftp commands to get the needed information / save the contents / then close the connection
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)
ftp.cwd(FOLDER)
ftp.dir(contents1.append)
ftp.quit()

# Building the string here
def buildStr(contents1, method):
    # had to make the extra contents list to be able to sort through if i should ignore the file or not
    contents = []

    if method == 7:
        finalString = ""
        # This loop looks at each file given, decides if we need to keep if, and if we keep it add to a new list
        while contents1:
            # The index here will always be 0 since i remove it when im done looking
            cut = contents1[0]

            # Filter that checks witch files to keep
            # If either of the first three digits aren't '-' delete that file from the list
            if cut[0] == 'd' or cut[0] == 'l':
                contents1.__delitem__(0)
            elif cut[1] == 'r':
                contents1.__delitem__(0)
            elif cut[2] == 'w':
                contents1.__delitem__(0)
            # If all of the first three digits are '-' add it to my new list
            else:
                cut = cut[:10]
                contents.append(cut)
                contents1.__delitem__(0)

        # This ignores the first three if we are basing this off of 7 bits
        # I am able do all the work in this loop because I know with method seven it will always be based on 7 bits
        for i in range(len(contents)):
            binary = ""

            # Here I cut the first three digits from the file permissions since they don't matter for this method
            cut = contents[i]
            cut = cut[3:]
            contents[i] = cut

            # Convert the remaining into binary
            for j in range(len(contents[i])):
                view = contents[i]
                if view[j] == '-':
                    binary += "0"
                else:
                    binary += "1"

            # covert the selected bits into the decimal version of that binary number
            byte = int(binary, 2)

            # if the byte is a backspace
            if (byte == 8):
                # remove the last character that was added to our text
                finalString = finalString[:-1]
            else:
                # adds any other character to our text
                finalString += chr(byte)

        # Clean up the results then print them
        print "_________________________"
        print "\n|    Secret Message     |"
        print "_________________________\n"
        print finalString
    elif method == 10:
        # Creating a string for both the 7-bit and 8-bit so I can print out both
        string7 = ""
        string8 = ""

        # Binary doesn't need reset after each run for this case
        binary = ""

        # This cuts everything but the first ten digits, keeping only the file permissions
        # No need to filter out the files for this case
        while contents1:
            cut = contents1[0]
            cut = cut[:10]
            contents.append(cut)
            contents1.__delitem__(0)

        # This puts together my binary string
        for i in range(len(contents)):

            for j in range(len(contents[i])):
                view = contents[i]
                if view[j] == '-':
                    binary += "0"
                else:
                    binary += "1"

        # Makes a copy so I can reuse this later
        binary1 = binary

        # This creates a byte for every 7 bits, converts it into an integer, then into a letter
        while binary1:
            byte = binary1[:7]
            binary1 = binary1[7:]
            byte = int(byte, 2)

            # if the byte is a backspace
            if (byte == 8):
                # remove the last character that was added to our text
                string7 = string7[:-1]
            else:
                # adds any other character to our text
                string7 += chr(byte)

        # This creates a byte for every 8 bits, converts it into an integer, then into a letter
        while binary:
            byte = binary[:8]
            binary = binary[8:]
            byte = int(byte, 2)


            # if the byte is a backspace
            if (byte == 8):
                # remove the last character that was added to our text
                string8 = string8[:-1]
            else:
                # adds any other character to our text
                string8 += chr(byte)

        # Clean up the results then print them
        print "_________________________"
        print "\n|    7-Bit Message      |"
        print "_________________________\n"
        print string7, "\n"
        print "_________________________"
        print "\n|    8-Bit Message      |"
        print "_________________________\n"
        print string8
    else:
        print "\nPlease enter a valid method."

        
buildStr(contents1, METHOD)
