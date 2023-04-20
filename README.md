# PyAutoGui Bing Search
This is a Python script that performs a random search on Bing using the PyAutoGui library. It clicks on the search box, types in a random string of letters and numbers, presses enter, waits for half a second, and then clears the search box.

## Installation
1. Clone the repository.
2. Install PyAutoGui using `pip install pyautogui` in your terminal.
3. Install keyboard using `pip install keyboard` in your terminal.

## Usage
1. Run `python main.py` in your terminal.
2. The script will start performing the searches.
3. Press `ESC` to quit the script.

## Customization
You can customize the following variables in the script:
- `x, y`: Coordinates of the Bing search box on your screen.
- `searchTotal`: Number of searches to perform.
- `randomLetters`: Characters to be used for generating the random search terms.
- `sleepTime`: Time to wait after each search (in seconds).
