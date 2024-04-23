import os

file_path = "/Users/christopherblystone/Documents/Joy of Coding/turing.txt"
lines = []
response = []
with open(file_path, "r") as file:
    content = file.read()
    print(content)


with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip())

response = lines[:2]+lines[-2:]
print(lines)
print()
print(*response)
print("end of main")


# selected_text = lines[:2] + lines[-2:]
