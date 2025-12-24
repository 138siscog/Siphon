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

#######################################################################################

## Updates — 12/22/2025

- feat: You are now able to place a flag.txt in any drive, your files  will be moved to the parent directory of the flag (currently limited to 1 flag only)
- issues: 
* This currently works only for match type 1, will apply to to other match cases soon
* This currently only still works with moving files in the cwd (current working directory) to parent directory of the flag
* If multiple flags found app just loops infinitly and files do not move, need to add edge cases for this
* 

### Notes
- Early flag system implemented for prototype
- Application currently scans only the current working directory and moves files to parent directory of flag location
- the flag will be located even if located in sub folder


#######################################################################################

# Updates — 12/23/2025

- feat: You are now able to place a flag.txt in any drive, your files  will be moved to the parent directory of the flag (currently limited to 1 flag only)
- issues: 
* The flag file is detected even if it is placed inside a subfolder.
* (Currently limited to a single flag file)

## known Issues 
- The application currently only moves files from the current working directory (CWD).
- If multiple flag.txt files are found, the application enters an infinite loop and files are not moved.
- Edge-case handling for multiple flags is planned.

### Notes
- Early flag-based destination system implemented as part of the prototype phase.
- Destination is determined by the parent directory of the detected flag file.
- Source scanning is intentionally limited to the current working directory for safety during early development.

#### Refactor
- Before adding new features, the codebase will be refactored to:
    - Remove duplicated logic
    - Improve readability and structure
    - Prepare for safer edge-case handling
- Development will continue regularly after the refactor phase.
