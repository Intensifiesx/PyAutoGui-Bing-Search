import pyautogui
import random
import keyboard

# Parameters to change
x, y = 252, 100  # Bing search box coordinates
searchTotal = 34  # Number of searches to perform
randomLetters = 'abcdefghijklmnopqrstuvwxyz1234567890'
search = ''  # Empty string to store search terms
sleepTime = 0.5  # Time to sleep between each search


# Decorator to check for ESC key press
def check_for_esc(func):
    def wrapper(*args, **kwargs):  # Wrapper function
        if keyboard.is_pressed('esc'):  # Check for ESC key press
            print('Quitting...')
            exit()
        return func(*args, **kwargs)
    return wrapper


@check_for_esc  # Decorate the function
def click(x, y):  # Wrapper function to click
    pyautogui.click(x, y)


@check_for_esc  # Decorate the function
def typewrite(text):  # Wrapper function to type text
    pyautogui.typewrite(text)


@check_for_esc  # Decorate the function
def press(key):  # Wrapper function to press a key
    pyautogui.press(key)


@check_for_esc  # Decorate the function
def sleep(seconds):  # Wrapper function to sleep
    pyautogui.sleep(seconds)


@check_for_esc  # Decorate the function
def hotkey(key1, key2):  # Wrapper function to press a hotkey
    pyautogui.hotkey(key1, key2)


# Loop through the search terms and perform the random search
# Press ESC to quit
for i in range(searchTotal):
    search += random.choice(randomLetters)
    click(x, y)
    typewrite(search)
    press('enter')
    sleep(sleepTime)

    # Clear the search box
    click(x, y)
    hotkey('ctrl', 'a')
    press('backspace')
