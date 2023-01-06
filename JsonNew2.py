import json

with open('accounts.json' ) as file:
    account = json.load(file)

print(json.dumps(account, indent=4))