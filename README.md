# AniMe matrix clock & battery level for linux

This script is designed to be used with asusctl to use the AniMe matrix on the Asus ROG Matrix laptops to show the current battery level, date and time.\
This works by creating an image with the current data every second and sending it to the display with asusctl.

# Install

1. Ensure you have [`asusctl`](https://asus-linux.org/asusctl/), `python3` and `pip` installed
1. Clone the git repo to a folder with `git clone https://github.com/florian-h05/anime-matrix-datetime-battery/`
1. cd into that folder with `cd anime-matrix-datetime-battery`
1. Install dependencies with `pip install -r requirements.txt`
1. Finally run the script with `python3 main.py`

## Credits

[Blobadoodle](https://github.com/Blobadoodle) for creating the original repo [Blobadoodle/anime-matric-clock](https://github.com/Blobadoodle/anime-matrix-clock)!

![ga401qc](.github/laptop.png)
