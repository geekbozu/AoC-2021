import os

depth = 0
with open("Day1/input.txt") as file:
    last = 0
    for line in file:
        if last == 0:
            last = line
            continue
        if int(line) > int(last):
            depth += 1
        last = line

print(depth)

# 1195
list = []
depth = 0
with open("Day1/input.txt") as file:
    for line in file:
        list.append(int(line))

last_sum = list[0] + list[1] + list[2]
list.pop(0)

for i in range(len(list) - 2):
    cur_sum = list[i] + list[i + 1] + list[i + 2]
    if cur_sum > last_sum:
        depth += 1
    last_sum = cur_sum

print(depth)

# 1235
