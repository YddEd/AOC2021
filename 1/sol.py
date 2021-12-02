def part_one(input_file):
    measurements = 0
    with open(input_file, "r") as f:
        input = f.readlines()
        i = 1
        while i < len(input):
            if int(input[i]) > int(input[i-1]):
                measurements += 1
            i += 1
    return measurements

# first attempt
def part_two(input_file):
    counter = 0
    with open(input_file, "r") as f:
        input = f.readlines()
        i = 3
        while i < len(input):
            first_window = int(input[i-3]) + int(input[i-2]) + int(input[i-1])
            second_window = int(input[i-2]) + int(input[i-1]) + int(input[i])
            if second_window > first_window:
                counter += 1
            i += 1
    return counter

# optimisation from SasCologne`
def part_two2(input_file):
    counter = 0
    with open(input_file, "r") as f:
        input = f.readlines()
        i = 3
        while i < len(input):
            if int(input[i]) > int(input[i-3]):
                counter += 1
            i += 1
    return counter

print(part_one("input.txt"))
print(part_two("input.txt"))
print(part_two2("input.txt"))