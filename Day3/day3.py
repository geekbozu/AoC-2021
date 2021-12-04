def part1_input(file):
    total = 1
    computed = [int(char) for char in file.readline().strip()]
    for line in file:
        row = [int(char) for char in line.strip()]
        computed = list(map(lambda a, b: a + b, computed, row))
        total += 1

    gamma = 0
    computed.reverse()
    for i, v in enumerate(computed):
        if v >= (total / 2):
            gamma += (2 ** i) * 1

    epsilon = gamma ^ ((2 ** len(computed)) - 1)

    return (gamma, epsilon, gamma * epsilon)


def part2_input(file):

    processed = []
    for line in file:
        row = [int(char) for char in line.strip()]
        processed.append(row)

    # most common mask
    ogr = processed
    csr = processed
    index = 0
    while len(ogr) > 1:
        computed = ogr[0]
        total = 1
        for entry in ogr[1:]:
            computed = list(map(lambda a, b: a + b, computed, entry))
            total += 1
        ogrmask = []
        for x in computed:
            if x >= (total / 2):
                ogrmask.append(1)
            else:
                ogrmask.append(0)

        ogr = [x for x in ogr if x[index] == ogrmask[index]]
        index += 1

    index = 0
    while len(csr) > 1:
        computed = csr[0]
        total = 1
        for entry in csr[1:]:
            computed = list(map(lambda a, b: a + b, computed, entry))
            total += 1

        csrmask = []
        for x in computed:
            if x < (total / 2):
                csrmask.append(1)
            else:
                csrmask.append(0)

        csr = [x for x in csr if x[index] == csrmask[index]]
        index += 1

    return (
        csr,
        ogr,
        int("".join([str(i) for i in ogr[0]]), 2)
        * int("".join([str(i) for i in csr[0]]), 2),
    )


# Day3 Part 1 Sample
# (22, 9, 198)
# =====================
# Day3 Part 1 My Input
# (3797, 298, 1131506)
# =====================
with open("Day3/sample.txt") as file:
    print("Day3 Part 1 Sample")
    print(part1_input(file))
    print("=====================")

with open("Day3/input.txt") as file:
    print("Day3 Part 1 My Input")
    print(part1_input(file))
    print("=====================")

# Day3 Part 2 Sample
# ([[0, 1, 0, 1, 0]], [[1, 0, 1, 1, 1]], 230)
# =====================
# Day3 Part 2 My Input
# ([[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1]], [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]], 7863147)
# =====================
with open("Day3/sample.txt") as file:
    print("Day3 Part 2 Sample")
    print(part2_input(file))
    print("=====================")

with open("Day3/input.txt") as file:
    print("Day3 Part 2 My Input")
    print(part2_input(file))
    print("=====================")
