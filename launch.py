from sys import argv
from os import system

commands = [
    "git pull",
    "git submodule update",
    "docker-compose build",
    "docker-compose down",
    f"docker-compose up -d --scale worker={argv[0]}"
]
[system(command) for command in commands]
