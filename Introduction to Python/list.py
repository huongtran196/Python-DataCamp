# Create a list
# area variables
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create a list areas
areas = [hall, kit, liv, bed, bath]
print(areas)

# Update the list
house = [['hallway', hall], 
        ['kitchen', kit], 
        ['living room', liv], 
        ['bedroom', bed], 
        ['bathroom', bath]]
print(house)
print(type(house))

# Subset & conquer
areas = ['hallway', 11.25,
        'kitchen', 18.0,
        'living room', 20.0,
        'bedroom', '10.75',
        'bathroom', 9.50]

# Print out the second element from areas
print(areas[1])

# Print out the last element from areas
print(areas[9])

# Print out the area of living room
print(areas[4:6])

# Subset & Calculate
eat_sleep_area = areas[3] + areas[7]
print(eat_sleep_area)
downstairs = areas[:6]
upstairs = areas[6:]
print(downstairs)
print(upstairs)

# Subsetting lists of lists
house[-1][1]
house[2][0]

# Manipulating lists
areas = ['hallway', 11.25, 
        'kitchen', 18.0, 
        'living room', 20.0, 
        'bedroom', 10.75, 
        'bathroom', 9.50]

areas[-1] = 10.50 # Update the size of the bathroom
areas[4] = 'chill zone' # Change the name of living room into chill zone
print(areas)


