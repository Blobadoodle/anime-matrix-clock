# Anime matrix clock for linux

This script is designed to be used with asusctl to use the anime matrix on the Asus Rog Matrix laptops to show the current time.\
This works by creating an image with the current time every minute and sending it to the display with asusctl.

# Install

First make sure you have asusctl and python3 and pip installed.\
Then clone the git repo to a folder with `git clone https://github.com/Blobadoodle/anime-matrix-clock/`\
Then cd into that folder with `cd anime-matrix-clock`\
Install the dependencies with `pip install -r requirements.txt` or with `pip install pillow pynput datetime`\
Finally run the script with `python3 main.py`

## Credits

[jakaco](https://github.com/jakaco) for testing.\
[source-foundry](https://github.com/source-foundry/) for the [font](https://github.com/source-foundry/Hack).

![ga401qc](.github/laptop.png)