horizontal_pos = 0
depth = 0

with open('input.txt') as file:
    lines = file.readlines()


# Part 1
# for line in lines:
#     split_line = line.split(' ')
#     if split_line[0] == "forward":
#         horizontal_pos += int(split_line[1])
#     elif split_line[0] == "down":
#         depth += int(split_line[1])
#     elif split_line[0] == "up":
#         depth -= int(split_line[1])
#     final_position = horizontal_pos * depth
# print(final_position)

# lines = ["forward 5", 'down 5', 'forward 8', 'up 3','down 8', 'forward 2']

# Part 2
aim = 0

for line in lines:
    split_line = line.split(' ')
    if split_line[0] == "down":
        aim += int(split_line[1])
    elif split_line[0] == "up":
        aim -= int(split_line[1])
    elif split_line[0] == "forward":
        horizontal_pos += int(split_line[1])
        depth += aim * int(split_line[1])

final_position = horizontal_pos * depth
print(final_position)