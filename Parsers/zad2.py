import json

with open('file.json') as f:
    data = json.load(f)

print(json.dumps(data, indent=4))

print("Want to delete some data?[y/n]")
ip = input()
if ip == 'y':
    print("Give user id:")
    idn = int(input())
    for pos, usr in enumerate(data):
        if usr["id"] == idn:
            data.pop(pos)

print("Want to add some data?[y/n]")
ip = input()
if ip == 'y':
    print("New id:")
    idn = int(input())
    print("New name:")
    name = input()
    print("New username:")
    username = input()
    print("New email:")
    email = input()
    data.append({"id": idn, "name": name, "username": username, "email": email})


with open('file.json', 'w') as outfile:
    json.dump(data, outfile)
