########################################################
##              Jimmie Gann, Brian Mckay              ##
##               Dr. Cherry CSC 132-002               ##
## __________________________________________________ ##
##             Student Atendance Checker              ##
##     This program allows students to log in then    ##
##    the professor can save the data to a database   ##
########################################################

###################################
## Importing Necessary Libraries ##
###################################

from hashlib import sha256
from math import *
from time import asctime
import os
import sys
import msvcrt

##################
## Global Stuff ##
##################

present = []
admin = {}

admin["cherry"] = 'j\xd4\xa6\xb1\xe5\xeaUiy^Qmq\x90\x9e\x0c\xe4\x80\x9d\x9d\xc9\x83\xd2\xc2\x19\x14OhO\x81n\x12' # = 1009

admin_file = open("admin_database.txt", "w")

admin_file.write(str(admin))
admin_file.close()
del admin_file

# This will see if the student database file exists in your library and if not will create the file
# Necessary because this is the only way to create a file the first time you run this program without causing an error
checkFile = "student_database.txt"

if os.path.isfile(checkFile):
    pass
else:
    old_studentdb_file = open("student_database.txt", "w")
    old_studentdb_file.write("{}")

    old_studentdb_file.close()
    del old_studentdb_file

#########################
## Necessary Functions ##
#########################

def resetPassword(name, newPin):
    students[name] = newPin
    new_studentdb_file = open("student_database.txt", "w")
    new_studentdb_file.write(str(students))
    new_studentdb_file.close()
    del new_studentdb_file
    print "\nThe students pin has been reset!"

def addStudent(name, pin):
    pin = sha256(str(pin)).digest()
    students[name] = pin
    new_studentdb_file = open("student_database.txt", "w")
    new_studentdb_file.write(str(students))
    new_studentdb_file.close()
    del new_studentdb_file
    print "\nNew student added to database!"

def removeStudent(name):
    new_studentdb_file = open("student_database.txt", "w")

    try:
        students.pop(name)
        print "\n\nStudent has been removed from the database."

    except:
        print "{} not found in database.".format(name)
        return

    new_studentdb_file.write(str(students))
    new_studentdb_file.close()
    del new_studentdb_file

def attendance():

    #This is so that i will be able to get the list of absent students
    allStudents = list(students)
    att_file = open("attendance_log.txt", "a")
    t = asctime()
    entry = t + " - Present: "
    counter = 0

    for i in present:
        counter += 1
        allStudents.remove(i)
        if (counter < len(present)):
            entry += i.capitalize() + ", "
        else:
            entry += i.capitalize()

    counter2 = 0
    entry += " --- Absent: "

    for i in allStudents:
        counter2 += 1
        if (counter2 < len(allStudents)):
            entry += i.capitalize() + ", "
        else:
            entry += i.capitalize()

    entry += "\n"

    att_file.write(entry)
    att_file.close()

    attendance = "Present:  "

    for i in present:
        counter += 1
        if (counter < len(present)):
            attendance += i.capitalize() + ", "
        else:
            attendance += i.capitalize()

    print attendance
    print "\nToday's attendance was also added to the database!"
    raw_input("Please press enter...")
    exit(0)

def asterisks():

    # This function is used to hide the password as it is being typed
    pin = ''

    while True:
        x = msvcrt.getch()
        if x == '\r':
            break
        sys.stdout.write('*')
        pin += x

    pin2 = int(pin)
    hashpin = str(sha256(str(pin2)).digest())


    return hashpin


###############
## Main Loop ##
###############

while(True):
    user = (raw_input("What is your name?\n")).lower()
    old_studentdb_file = open("student_database.txt", "r")
    admin_file = open("admin_database.txt", "r")

    students = eval(old_studentdb_file.read())
    admin = eval(admin_file.read())

    admin_file.close()
    old_studentdb_file.close()
    del old_studentdb_file
    del admin_file

    if (user in admin):

        counter = 0

        print "Enter your password: "
        hashpin = asterisks()

        while True:

            Continue = False

            if (hashpin == admin.get(user) ):
                print "\n   Admin Menu\n_________________"
                getOption = raw_input("\nWould you like to ADD STUDENT, REMOVE STUDENT, RESET A PASSWORD, or CHECK ATTENDANCE? \n").lower()

                if (getOption == "add student"):
                    newStudent = raw_input("\nNew student name: \n")
                    newPin = raw_input("\nEnter their new pin: \n")

                    if (len(newPin) == 4):
                        addStudent(newStudent, newPin)

                    else:
                        newPin = raw_input("Enter a pin of exactly 4 digits: ")

                    answer = raw_input("Is there something else you would like to do? ").lower()

                    while True:
                        if (answer == "no" or answer == "n"):
                            break
                        elif (answer == "yes" or answer == "y"):
                            break
                        else:
                            answer = raw_input("Please type yes or no: ")

                    if (answer == "no" or answer == "n"):
                        print "\n__________________\n"
                        break
                    elif (answer == "yes" or answer == "y"):
                        Continue = True

                if (getOption == "remove student"):
                    name = raw_input("\nWhich student would you like to remove? \n")
                    check = raw_input("\nAre you sure you would like to remove " + str(name).upper() + " from your roll sheet? \n")

                    while True:
                        if (check == 'yes' or check == 'y'):

                            counter = 0
                            print "\nPlease re-enter your password to confirm: "
                            hashpin = asterisks()


                            if (hashpin == admin.get(user)):
                                removeStudent(name)
                                break
                            else:
                                print "Wrong pin, Please try again."

                        elif (check == "no" or check == "n"):
                            print "The student was not removed."
                            break

                        else:
                            print "Please type yes or no"

                    answer = raw_input("Is there something else you would like to do? \n").lower()

                    while True:
                        if (answer == "no" or answer == "n"):
                            break
                        elif (answer == "yes" or answer == "y"):
                            break
                        else:
                            answer = raw_input("Please type yes or no: ")

                    if (answer == "no" or answer == "n"):
                        print "\n__________________"
                        break
                    elif (answer == "yes" or answer == "y"):
                        Continue = True

                if (getOption == "reset a password"):
                    name = raw_input("\nWhich student would you like to reset? \n")
                    check = raw_input("\nAre you sure you would like to reset " + str(name).upper() + "'s password? \n")

                    while True:
                        if (check == 'yes' or check == 'y'):

                            counter = 0
                            print "\nPlease re-enter your password to confirm: "
                            hashpin = asterisks()


                            if (hashpin == admin.get(user)):
                                pin = input("\n\nWhat is the students new pin? \n")
                                newPin = sha256(str(pin)).digest()
                                resetPassword(name, newPin)
                                break
                            else:
                                print "Wrong pin, Please try again."

                        elif (check == "no" or check == "n"):
                            print "The student was not reset."
                            break

                        else:
                            print "Please type yes or no"

                    answer = raw_input("Is there something else you would like to do? \n").lower()

                    while True:
                        if (answer == "no" or answer == "n"):
                            break
                        elif (answer == "yes" or answer == "y"):
                            break
                        else:
                            answer = raw_input("Please type yes or no: ")

                    if (answer == "no" or answer == "n"):
                        print "\n__________________"
                        break
                    elif (answer == "yes" or answer == "y"):
                        Continue = True

                if (getOption == "check attendance"):
                    attendance()

                    answer = raw_input("Is there something else you would like to do? ").lower()

                    while True:
                        if (answer == "no" or answer == "n"):
                            break
                        elif (answer == "yes" or answer == "y"):
                            break
                        else:
                            answer = raw_input("Please type yes or no: ")

                    if (answer == "no" or answer == "n"):
                        print "\n__________________"
                        break
                    elif (answer == "yes" or answer == "y"):
                        Continue = True

                elif (Continue == True):
                    pass

                else:
                    print "\nIncorrect input, please type: ADD STUDENT, REMOVE STUDENT, or CHECK ATTENDANCE"



            else:
                print "\nIncorrect password, please try again: "
                hashpin = asterisks()

    elif (user in students):

        while True:

            if (user in present):
                print "You are already signed in for today"

            else:

                trys = 0

                while True:

                    print "Enter your password: "
                    hashpin = asterisks()

                    if (hashpin != students.get(user) and trys <= 3):
                        print "\nThis pin is incorrect, please try again"
                        trys += 1

                    elif (hashpin == students.get(user)):
                        print "\nWelcome back {}\n".format(str(user)) + "____________________\n"
                        present.append(user)
                        break

                    elif (trys > 3):
                        print "\nToo many failed attempts, try again later"
                        break

                break

    else:
        print "Student not found in our database!\n__________________________________\n"