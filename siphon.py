import os
import shutil
from pathlib import Path

file_types = {
    "*.txt",
    "*.js",
    "*.svg",
    "*.png",
    "*.jpeg",
    "*.gif",
    "*.tiff",
    "*.pdf",
    "*.wmf",
    "*.eps",
    "*.exr",
    "*.hdr",
    "*.tda"
}

video_types = {
    "*.mp4",
    "*.mov",
    "*.mkv",
    "*.avi",
    "*.wmv",
    "*.webm",
}

all_files = {
    "*.mp4",
    "*.mov",
    "*.mkv",
    "*.avi",
    "*.wmv",
    "*.webm",
    "*.txt",
    "*.js",
    "*.png",
    "*.jpeg",
    "*.gif",
    "*.tiff",
    "*.pdf",
    "*.svg",
    "*.wmf",
    "*.eps",
    "*.exr",
    "*.hdr",
    "*.tda"
}
 
while True:

    print("Welcome to Siphon!")

    print("\n")

    input("Before proceeding, ensure you have placed a txt file named 'flag' inside the drive you want the files to be moved to, \npress enter when ready")
    
    print("\n")
    
    print("Select the files to move\n1. Files and Images\n2. Videos\n3. Images, Files and Videos\n4. Custom Files\n5. Exit")
    print('\n')
    choice = int(input(":"))

    # Def to search for flags in most common drive letters, making C last as its usually the largest drive to search

    def search_flag_on_drives(filename):
        drives = ['H:', 'G:', 'F:', 'E:', 'D:', 'C:']
        found_flag = []

        for drive in drives:
            drive_path = Path(drive)
            if drive_path.exists():
                matches = drive_path.rglob(filename)
                found_flag.extend(matches)
        
        return(found_flag)

    # main App loop begins

    match choice:
        case 1:
            #Searches Drives for flag.txt 

            files = search_flag_on_drives("flag.txt")
            for file in files:

                #takes parent location of flag.txt and turns it into varialbel to use in the next section     
                          
                file_path = Path(file).resolve()
                parent_directory = file_path.parent

            # Temporarily only moves files in our cwd, but it moves the files to the parent location of where the flag was located

            for i in file_types:
                for file_path in Path.cwd().glob(i):
                    new_path = Path(fr'{parent_directory}') / file_path.name
                    shutil.move(str(file_path), str(new_path))

            #note, i tested putting the flag.txt in a sub folder and program is working as expected
            
            print("\n")
            print("Move Complete!")
            print("\n")
            print("Thank you for using Siphon!")
            break
        
        case 2:
            #Searches Drives for flag.txt 
            files = search_flag_on_drives("flag.txt")
            for file in files:

            #takes parent location of flag.txt and turns it into varialbel to use in the next section     
                          
                file_path = Path(file).resolve()
                parent_directory = file_path.parent

             # Temporarily only moves files in our cwd, but it moves the files to the parent location of where the flag was located

            for i in video_types:
                for file_path in Path.cwd().glob(i):
                    new_path = Path(fr'{parent_directory}') / file_path.name
                    shutil.move(str(file_path), str(new_path))
            
            print("\n")
            print("Move Complete!")
            print("\n")
            print("Thank you for using Siphon!")
            break
        
        case 3:
            #Searches Drives for flag.txt 
            files = search_flag_on_drives("flag.txt")
            for file in files:

            #takes parent location of flag.txt and turns it into varialbel to use in the next section     
                          
                file_path = Path(file).resolve()
                parent_directory = file_path.parent

             # Temporarily only moves files in our cwd, but it moves the files to the parent location of where the flag was located

            for i in all_files:
                for file_path in Path.cwd().glob(i):
                    new_path = Path(fr'{parent_directory}') / file_path.name
                    shutil.move(str(file_path), str(new_path))
            
            print("\n")
            print("Move Complete!")
            print("\n")
            print("Thank you for using Siphon!")
            break

        case 4:
            custom_files = set()

            #Searches Drives for flag.txt 
            files = search_flag_on_drives("flag.txt")
            for file in files:

            #takes parent location of flag.txt and turns it into varialbel to use in the next section     
                          
                file_path = Path(file).resolve()
                parent_directory = file_path.parent

            # Temporarily only moves files in our cwd, but it moves the files to the parent location of where the flag was located

            while True:

                filetype = input("add the file type you want to relocate in '*.filetype' format example: .svg, .js, .py\n:")
                
                custom_files.add(f"*{filetype}")

                looped = input("Would you like to add another file type? y/n\n:").lower()
                if looped != "n":
                    continue
                
                for i in custom_files:
                    for file_path in Path.cwd().glob(i):
                        new_path = Path(fr'{parent_directory}') / file_path.name
                        shutil.move(str(file_path), str(new_path))

                print("Move Complete!")
                print("\n")
                print("Thank you for using Siphon!")
                exit()
                   
        case 5:
            exit()
