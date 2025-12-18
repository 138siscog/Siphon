import os
from pathlib import Path
 

file_types = {
    "*.txt",
    "*.js",
    "*.svg"
}

for i in file_types:
    for file_path in Path.cwd().glob(i):
        new_path = Path(r"#Insert file Path") / file_path.name
        file_path.replace(new_path) 