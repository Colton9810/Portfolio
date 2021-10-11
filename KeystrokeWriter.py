# This will allow you to "type" on someones computer with the characters you tell it to type
from pynput.keyboard import Key, Controller
from time import sleep
import termios

keyboard = Controller()
password = input()
timings = input()

password = password.split(", ")
password = password[:len(password) // 2 + 1]
password = "".join(password)

timings = timings.split(", ")
timings = [float(a) for a in timings]
keypress = timings[:int(len(timings) // 2 + 1)]
keyintervals = timings[len(timings) // 2 + 1:]

# print("keypress: {}, keyintervals: {}".format(len(keypress), keyintervals))
sleep(5)

for i in range(len(password)):

    keyboard.press(password[i])
    sleep(keypress[i])
    keyboard.release(password[i])

    if i == len(password) - 1:
        pass
    else:
        sleep(keyintervals[i])

keyboard.press(Key.enter)
keyboard.release(Key.enter)
