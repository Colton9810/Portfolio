import csv, uuid, pytz, pandas
from hashlib import sha256
from datetime import datetime

NAMESPACE = uuid.UUID('{d9b2d63da2334123847a76838bf2413a}')
TIMEZONE = pytz.timezone('Etc/GMT+6')

names = "database_dump.csv"  # input("Enter the name of the hashed database(+ extension): ")
d_name = "dictionary.txt"  # input("Enter the name of the dictionary(+ extension): ")

d = open(d_name, "r")
d = d.read().splitlines()

# reads from the dump file and adds each given
# uuid, hash, and encoded timestamp to the appropriate array
def create_lists():

    uuids = []
    passwords = []
    times = []

    wb = open(names, newline="")
    spamreader = csv.reader(wb, delimiter=' ', quotechar='|')

    for i in spamreader:
        curr = str(i)
        uuids.append(curr[2:38])
        passwords.append(curr[39:103])
        times.append(curr[104:-2])

    uuids.remove(uuids[0])
    passwords.remove(passwords[0])
    times.remove(times[0])

    return uuids, passwords, times

# compares each of the the values in the plain text
# dictionary to the uuid values
def get_names(plaintxt_name_db, uuids):

    counter = 0

    for i in d:
        name_uuid = uuid.uuid5(NAMESPACE, i)

        if str(name_uuid) in uuids:
            x = uuids.index(str(name_uuid))         # x is the index of the uuid from the dump file
            plaintxt_name_db[x] = i                 # we keep track of this to accurately pair usernames, passwords, and times
            counter += 1
        if counter == len(uuids):           # here we will break out of the loop once we found all of the usernames
            break

    return plaintxt_name_db

# this functions operates the same way as the get_names function
def get_passwords(plaintxt_password, passwords):

    counter = 0

    for i in d:
        temp_hash = sha256(i.encode('utf-8')).hexdigest()
        temp_hash = temp_hash.upper()

        if temp_hash in passwords:
            x = passwords.index(temp_hash)
            plaintxt_password[x] = i
            counter += 1
        if counter == len(passwords):
            break

    return plaintxt_password

# function that calculates the elasped time from epoch using the given time (in sec)
def get_times(plaintxt_times, times):

    for time in times:
        plaintxt_times.append((datetime.fromtimestamp(int(time))).astimezone(TIMEZONE).isoformat())

    return plaintxt_times

# organizes all of our data into a dataframe using the pandas library
def pandas_df(names, passwords, times):

    df = pandas.DataFrame()
    nm = pandas.Series(names)
    pw = pandas.Series(passwords)
    lat = pandas.Series(times)

    df['Names'] = nm.values
    df['Passwords'] = pw.values
    df['Last Access Time'] = lat.values

    return df

##################
## Main Program ##
##################


uuids, passwords, times = create_lists()

# we create arrays of n length to properly insert our data at the correct index
plaintxt_password = [None] * len(passwords)
plaintxt_name_db = [None] * len(uuids)
plaintxt_times = []                         # this is empty because all of the timestamps stay in the order we get them

plaintxt_name_db = get_names(plaintxt_name_db, uuids)
plaintxt_password = get_passwords(plaintxt_password, passwords)
plaintxt_times = get_times(plaintxt_times, times)

print(pandas_df(plaintxt_name_db, plaintxt_password, plaintxt_times))
