from os import chdir, system
from pathlib import Path

current_dir = Path()
for directory in current_dir.glob("*"):
    if not directory.is_dir():
        continue
    chdir(str(directory))
    system("git pull")
    chdir("../")
