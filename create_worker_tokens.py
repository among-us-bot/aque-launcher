"""
Created by Epic at 11/5/20
"""
from ujson import dumps

tokens = {}

while True:
    worker_name = input("Name (cancel to cancel)> ")
    worker_token = input("Token> ")

    if worker_name == "cancel":
        print(dumps(tokens))
        break
    tokens[worker_name] = worker_token
