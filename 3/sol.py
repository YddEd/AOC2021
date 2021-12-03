def part_one(input_file):
    gamma = ""
    epsilon = ""

    with open(input_file, "r") as f:
        input = f.readlines()

    bit_length = len(input[0].strip())
    bits = {x+1: 0 for x in range(bit_length)}
    num_lines = len(input)
    
    for line in input:
        for i, bit in enumerate(line.strip()):
            bits[i+1] += int(bit)
    
    for count in bits.values():
        if count > (num_lines - count):
            gamma += "1"
            epsilon += "0"
        elif count < (num_lines - count):
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)

print(part_one("sample.txt"))
print(part_one("input.txt"))