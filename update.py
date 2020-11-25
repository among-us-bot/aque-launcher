from os import chdir, system
from pathlib import Path
from sys import argv

current_dir = Path()
for directory in current_dir.glob("*"):
    if not directory.is_dir():
        continue
    chdir(str(directory))
    print(f"Updating {directory}!")
    system("git pull origin master")
    chdir("../")

if "--commit" in argv:
    system("git add .")
    system("git commit -m 'Dependencies: Update modules'")
    system("git push")

