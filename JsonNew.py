import json

with open("accounts.json"), "r" as f:
    data = json.load(f)

print(data)

