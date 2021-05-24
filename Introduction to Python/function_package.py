# Create variable var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out the type of var1
print(type(var1))

# Print out the length of var1
print(len(var1))

# Convert var2 into interger: out2
out2 = int(var2)

# Create 2 lists
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

full = first + second
full_sorted = sorted(full, reverse= True) # Sort full list in descending order
print(full_sorted)

# String Method: upper() & count()
place = 'poolhouse'
place_up = place.upper()

print(place_up)
print(place)
print(place.count('o'))

# List Method: index() & count()
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

print(areas.index(20.0)) # Print out the position of the element 20.0
print(areas.count(9.50)) # Print out how often 9.50 appear in the list

# List Method: append() & reverse() & remove()
areas.append(24.5)
areas.append(15.45)
areas.reverse()
print(areas)

# Definition of radius
r = 0.43

# Import the math package
import math 

# Calculate C
C = 2 * r * math.pi

# Calculate A
A = math.pi * r * r

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)
