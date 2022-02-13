import ctypes
from threading import Thread
from PIL import Image
from PIL import ImageGrab
from win32.win32gui import GetWindowRect, GetWindowText, EnumWindows
import pytesseract
import numpy as np
import pyscreenshot as ImageGrab
import time
import pyautogui
import mouse
import mss
import mss.tools

# First we focus the window for in-game inputs
# when running script, minecraft needs to be in the background (be able to alt+tab **once** to focus screen)

toplist, winlist = [], []


def enum_cb(hwnd, results):
    winlist.append((hwnd, GetWindowText(hwnd)))


EnumWindows(enum_cb, toplist)

minec = [(hwnd, title)
         for hwnd, title in winlist if 'minecraft' in title.lower()]
minec = minec[0]
hwnd = minec[0]

# SetForegroundWindow(hwnd)

bbox = GetWindowRect(hwnd)
# Holds down the alt key
pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")
pyautogui.press("esc")
pyautogui.keyDown('e')
time.sleep(2)
pyautogui.keyDown('e')
time.sleep(2)

# START SECTION FOR MANAGING INPUTS


SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions for handling inputs


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002,
                        0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# END


def main():

    # directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html <== this link is RIP unfortunately
    PressKey(0x12)

    ReleaseKey(0x12)
    while (True):
        time.sleep(0.75)
        with mss.mss() as sct:
            # grabbing part of the screen which has the narration text
            monitor = {"top": 600, "left": 1250, "width": 250, "height": 150}
            img_array = (sct.grab(monitor))
            print('Catching fish...')
            text = pytesseract.image_to_string(np.array(img_array))
            # debug if not catching correctly by checking below print(text) when a fish is on the line
            # might need to adjust IF statement to include extra phrases.
            # print(text)
            img = Image.frombytes("RGB", img_array.size,
                                  img_array.bgra, "raw", "BGRX")

        # include extra phrases in if statement if OCR is inconsistent
        if 'Fishing Bobber splashes' in text or ('Bobber' in text and 'splashes' in text):
            output = "caught-a-fish-" + str(time.time()) + ".png"
            print('Caught one!')
            print('Casting!')
            img.save(output)
            mouse.click('right')
            time.sleep(0.5)
            mouse.click('right')
            monitor = {"top": 600, "left": 600, "width": 700, "height": 150}
            img_array = (sct.grab(monitor))
            img = Image.frombytes("RGB", img_array.size,
                                  img_array.bgra, "raw", "BGRX")
            output = "casting-look-at-xp-" + str(time.time()) + ".png"
            img.save(output)

    # print(text)


main()
