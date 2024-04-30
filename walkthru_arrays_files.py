file = open("/Users/christopherblystone/Documents/Joy of Coding/turing.txt")
lines = []
for line in file:
    lines.append(line)
file.close


print(lines[:2])
print(lines[-2:])
