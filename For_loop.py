# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))


    # house list of lists
    house = [["hallway", 11.25],
             ["kitchen", 18.0],
             ["living room", 20.0],
             ["bedroom", 10.75],
             ["bathroom", 9.50]]

    # Build a for loop from scratch
    for x in house:
        print("the " + x[0] + "is " + str(x[1]) + " sqm")