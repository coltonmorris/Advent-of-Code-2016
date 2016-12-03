# read input file
with open('tmp.txt', 'r') as file:
    data = file.read()

current_number = 1
number_map = {
        # Up, down, left, right
    1: [None, 4, None, 2],
    2: [None, 5, 1, 3],
    3: [None, 6, 2, None],
    4: [1, 7, None, 6],
    5: [2, 8, 4, 6],
    6: [3, 9, 5, None],
    7: [4, None, None, 8],
    8: [5, None, 7, 9],
    9: [6, None, 8, None],
}

for line in data.split("\n")[:-1]:
    for char in line:
        if char == "U":
            print number_map[current_number][0]
            if number_map[current_number][0]:
                print "worked"
            else:
                print 'nope'
        if char == "D":
            print 'd'
        if char == "L":
            print 'l'
        if char == "R":
            print 'r'


