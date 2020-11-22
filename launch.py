from sys import argv
from os import system
print(f"Launching using {argv[1]} workers")
commands = [
    "git pull",
    "git submodule update",
    "docker-compose build",
    "docker-compose down",
    f"docker-compose up -d --scale worker={argv[1]}"
]
[system(command) for command in commands]
