SIPHON V0.1.0

***Siphon is a file relocator im building using the pathlib library, the end goal is to have this program scan all mounted drives accessible to the user and move files from their current location to the selected location, this is still in very early protoype***

***Currently the build just loops through a for loop and it looks for the specified file types in the root folder and moves them to the fodler named destination, you can move the desitnation folder to any location in your computer and in the Path(r"#Insert file Path") insert the file path its located, ensure to leave the r before the "filepath", Important to note that This hardcoded destination will be replaced by the flag-based system in a future version.***

**In the file_types tuple you can add more file extension using the format "*.filetype" for example "*.mp4" or "*.mp3" if you are adding multiple ensure to add commas between the file types or it will result in an error**

-----Files in Root-----
**Currently there are a few files in the root directory named flag, flag2, flag3, test.js, github. These are test files i was using to figure out how this library works and how files are moved, these files will not be in the final build they were just for testing.**

-----Design Doc-----
**I have included a design doc for an example of how i want the project to work, this is located in the docs folder, its a bit messy and i know some parts are missing in terms of going into the depth explaining what is happening, i will be sure to revisit and update the file as needed**

- flag clarification, at the begining of the design doc it says "Set txt file named flag.txt where files will end up"

**The idea behind this is that you can insert a flash drive or hard drive create a blank text file named flag.txt and the program will scan the computer for this file once you decided you file movement option, the flag will let the program know "this is where i want all the files to be located"**

- If there is more than one flag at a time, you will be promted to select which to use, it will not guess or assume which to use. 

- when backing up the program will exclude drive and file path where flag is located, 

- if no flag is detected, the prgram will let you know its missing and ask you to set one and rerun when ready**

- permission issues, you will be notified before scan begins that there may be some issues 

**Im still learning how this librabry works and i will update as much as i can, the goal is not to finish this quick but to ensure i grasp how the library works and ensure my programing skills are improving.**


## Updates — 12/18/2025

- feat: add custom filetype selection using sets
- fix: process all custom filetypes before exiting custom mode

### Notes
- Early match-case workflow implemented for prototype
- Application currently scans only the current working directory
- Subdirectory traversal is not yet implemented (planned as part of learning pathlib)
