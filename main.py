import pyautogui
import random
import string

i = 1
while i < 6:
    up = random.randint(1, 1080)

    down = random.randint(1, 1920)

    letter = random.choice(string.ascii_letters)

    pyautogui.FAILSAFE = False

    pyautogui.moveTo(up, down)
    pyautogui.typewrite(letter)
