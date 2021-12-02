measurements = 0
with open("input.txt", "r") as f:
    input = f.readlines()
    i = 1
    while i < len(input):
        if int(input[i]) > int(input[i-1]):
            measurements += 1
        i += 1
print(measurements)