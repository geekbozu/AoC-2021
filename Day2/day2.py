
def part1_input(file):
    depth = 0
    horiz = 0
    for motion in file:
        act = motion.split(" ")
        match act[0]:
            case 'forward':
                horiz += int(act[1])
                
            case 'down':
                depth += int(act[1])
                
            case 'up':
                depth -= int(act[1])
    return (horiz,depth,horiz*depth)     

def part2_input(file):
    depth = 0
    horiz = 0
    aim =0
    for motion in file:
        act = motion.split(" ")
        match act[0]:
            case 'forward':
                depth += aim*int(act[1])
                horiz += int(act[1])
                
            case 'down':
                aim += int(act[1])
            case 'up':
                aim -= int(act[1])
    return (horiz,depth,horiz*depth)     


# Day2 Part 1 Sample
# (15, 10, 150)
# =====================
# Day2 Part 1 My Input
# (1909, 655, 1250395)
# =====================
with open("Day2/sample.txt") as file:
    print("Day2 Part 1 Sample")
    print(part1_input(file))
    print("=====================")

with open("Day2/input.txt") as file:
    print("Day2 Part 1 My Input")
    print(part1_input(file))
    print("=====================")

# Day2 Part 2 Sample
# (15, 60, 900)
# =====================
# Day2 Part 2 My Input
# (1909, 760194, 1451210346)
# =====================
with open("Day2/sample.txt") as file:
    print("Day2 Part 2 Sample")
    print(part2_input(file))
    print("=====================")

with open("Day2/input.txt") as file:
    print("Day2 Part 2 My Input")
    print(part2_input(file))
    print("=====================")
