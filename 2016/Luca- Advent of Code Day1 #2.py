instruction = ["R3", "L5", "R1", "R2", "L5", "R2", "R3", "L2", "L5", "R5", "L4", "L3", "R5", "L1", "R3", "R4", "R1", "L3", "R3", "L2", "L5", "L2", "R4", "R5", "R5", "L4", "L3", "L3", "R4", "R4", "R5", "L5", "L3", "R2", "R2", "L3", "L4", "L5", "R1", "R3", "L3", "R2", "L3", "R5", "L194", "L2", "L5", "R2", "R1", "R1", "L1", "L5", "L4", "R4", "R2", "R2", "L4", "L1", "R2", "R53", "R3", "L5", "R72", "R2", "L5", "R3", "L4", "R187", "L4", "L5", "L2", "R1", "R3", "R5", "L4", "L4", "R2", "R5", "L5", "L4", "L3", "R5", "L2", "R1", "R1", "R4", "L1", "R2", "L3", "R5", "L4", "R2", "L3", "R1", "L4", "R4", "L1", "L2", "R3", "L1", "L1", "R4", "R3", "L4", "R2", "R5", "L2", "L3", "L3", "L1", "R3", "R5", "R2", "R3", "R1", "R2", "L1", "L4", "L5", "L2", "R4", "R5", "L2", "R4", "R4", "L3", "R2", "R1", "L4", "R3", "L3", "L4", "L3", "L1", "R3", "L2", "R2", "L4", "L4", "L5", "R3", "R5", "R3", "L2", "R5", "L2", "L1", "L5", "L1", "R2", "R4", "L5", "R2", "L4", "L5", "L4", "L5", "L2", "L5", "L4", "R5", "R3", "R2", "R2", "L3", "R3", "L2", "L5"]
#instruction = ["R8", "R4", "R4", "R8"] #Experimenting
direction = 0
x = 0
y = 0
coordinates = []
firstMatchX = 0
firstMatchY = 0
matches = 0

def check():
    if "{}, {}".format(x, y) in coordinates:
        #if matches < 1:
            global matches
            matches += 1
            print("Match Found!")
            print("x")
            print(x)
            print("y")
            print(y)
            if matches == 1:
                global firstMatchX
                global firstMatchY
                firstMatchX = x
                firstMatchY = y
 
    coordinates.append("{}, {}".format(x, y))
    #print(coordinates)

for w in instruction:
    #print(w)
    if w[0] == "R":
        #print("Right")
        direction += 1
        if direction == 4:
            direction = 0
        #print(direction)
        
    elif w[0] == "L":
        #print("Left")
        direction -= 1
        if direction == -1:
            direction = 3
        #print(direction)

    if direction == 0:
        for i in range(int(w[1:])):
            y += 1
            check()
        #print(y)
        #print("y")

    if direction == 1:
        for i in range(int(w[1:])):
            x += 1
            check()
        #print(x)
        #print("x")

    if direction == 2:
        for i in range(int(w[1:])):
            y -= 1
            check()
        #print(y)
        #print("y")
                
    if direction == 3:
        for i in range(int(w[1:])):
            x -= 1
            check()
        #print(x)
        #print("x")

    #print("x" + str(x))
    #print("y" + str(y))
    

print("Co-ordinate for firstMatchX is " + str(firstMatchX))
print("Co-ordinate for firstMatchY is " + str(firstMatchY))
print("Co-ordinate for x is " + str(x))
print("Co-ordinate for y is " + str(y))
print("Therefore the distance between the points is " + str((abs(0 - x) + abs(0 - y))))
print("Therefore the distance between your location and the first double visit is " + str((abs(0 - firstMatchX) + abs(0 - firstMatchY))))
