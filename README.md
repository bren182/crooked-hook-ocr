# The crooked hook MC Auto-fisher OCR 🪝

## Usage

This application was tested using `python 3.9.6`

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

[] Add optional launch flags for saving images of captures and xp progress
[] Add folder structures for saved images
[] Revise alt-tab + focusing on minecraft window approach
[] Implement settings for full-screen + custom window sizes
