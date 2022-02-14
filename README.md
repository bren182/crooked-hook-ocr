# The crooked hook MC Auto-fisher OCR 🪝

## Usage & Installation

Run `pip install -r requirements.text`. 

This application was tested using `python 3.9.6`. The application depends on the Minecraft narrator being enabled. For enabling Minecraft Narrator, please see following link: https://ipoki.com/how-to-turn-off-narrator-in-minecraft/

This app also requires tesseract-ocr to be installed on the system. Download to .exe for 64 bit here: eetesseract is not installed or it's not in your PATH. See README file for more information https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.1.20220118.exe . 

Also make sure that the Tesseract-OCR folder is in your System Environment Variables `PATH`. 

- 1 Download crooked-hook.py into a new folder.
- 2 Open command prompt or Windows Powershell as admin and `cd` to folder where crooked-hook.py is located.
- 3 Open minecraft and log into a world.
- 4 NB: Minimize minecraft by opening Inventory.
- 5 Run the following command `python crooked-hook.py` in the command prompt/powershell window

(The script will run and do the following:

- alt-tab to Minecraft screen,
- press E to close the inventory screen automatically,
- and begin monitoring for fishing.)

- 7 When able, in Minecraft, walk to your nearest pond and cast a line.
- 8 Sit back, relax, profit.

## Known issues

Currently only works with minimized window and 1900x1080 screen resolution. Resolution variable for window needs to be set manually. Sometimes when a catch is detected, casting happens twice. Recommended to use a fishing rod with at least mending.

## To-do

- [ ] Add optional launch flags for saving images of captures and xp progress
- [ ] Add folder structures for saved images
- [ ] Revise alt-tab + focusing on minecraft window approach
- [ ] Implement settings for full-screen + custom window sizes
- [ ] Clearer instructions for setting up Minecraft to run app (enable narrator, window size, etc). 
