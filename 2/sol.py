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

print(part_one("input.txt"))