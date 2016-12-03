current_direction = "N"
current_location = [0,0]
visited_locations = [[0,0]]

# helper function for changing our direction
def change_direction (direction):
    # map for changing directions. The first index is the result of turning left, while the second index is the result of turning right.
    direction_map = {
        "N": ["W","E"],
        "S": ["E","W"],
        "E": ["N","S"],
        "W": ["S","N"],
    }
    global current_direction

    direction_map[current_direction]
    if direction == "L":
        current_direction = direction_map[current_direction][0]
    if direction == "R":
        current_direction = direction_map[current_direction][1]

# helper function for moving us a certain number of spaces
def travel (distance, direction):
    global visited_locations
    global current_location

    # walk the distance
    for num in range(distance):
        if direction == "N":
            current_location[1] += 1
        if direction == "S":
            current_location[1] -= 1
        if direction == "E":
            current_location[0] += 1
        if direction == "W":
            current_location[0] -= 1

        # stop walking if we've been here
        if current_location in visited_locations:
            print 'current_location summed: ' + str((current_location[0] + current_location[1]))
            exit()

        # save the locations we have been at
        visited_locations.append(current_location[:])


# read input file
with open('input.txt', 'r') as file:
    data = file.read()

# remove newline character from input data and split into a list
data = data[:-1].split(', ')

# execute each move until we visit the same place twice
for move in data:
    change_direction(move[0])
    travel(int(move[1:]),current_direction)

print 'current_location summed: ' + str((current_location[0] + current_location[1]))
