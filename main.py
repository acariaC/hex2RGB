hexInput = input("Enter a list of hex colors:")
hexSplit = hexInput.replace('#', "").split()
rgb = []
print(hexSplit)

for element in hexSplit:
    red = int(element[0], 16) * 16 + int(element[1], 16)
    green = int(element[2], 16) * 16 + int(element[3], 16)
    blue = int(element[4], 16) * 16 + int(element[5], 16)
    rgb.append([red, green, blue])

print(rgb)
