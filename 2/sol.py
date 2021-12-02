def part_one(input_file):
    horizontal = 0
    depth = 0

    with open(input_file, "r") as f:
        input = f.readlines()
        for line in input:
            direction = line.split()[0]
            units = int(line.split()[1])
            if direction == "forward":
                horizontal += units
            elif direction == "down":
                depth += units
            elif direction == "up":
                depth -= units

    return horizontal * depth

def part_two(input_file):
    horizontal = 0
    depth = 0
    aim = 0

    with open(input_file, "r") as f:
        input = f.readlines()
        for line in input:
            direction = line.split()[0]
            units = int(line.split()[1])
            if direction == "forward":
                horizontal += units
                depth += aim * units
            elif direction == "down":
                aim += units
            elif direction == "up":
                aim -= units

    return horizontal * depth

print(part_one("sample.txt"))
print(part_one("input.txt"))
print(part_two("sample.txt"))
print(part_two("input.txt"))