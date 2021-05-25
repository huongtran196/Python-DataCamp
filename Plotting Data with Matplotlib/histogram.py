# Create a histogram of the column 'weight' from the DataFrame 'puppies'
import matplotlib.pyplot as plt
plt.hist(puppies.weight)

# Change the number of bins to 50 and range from 5 to 35
plt.hist(puppies.weight, bins = 50, range = (5,35))

# Add label
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()

# Create second histogram 
plt.hist(gravel.radius, bins = 40, range = (2,8), density = True)

plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

plt.show()

plt.hist(life_exp, bins=15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins=15)

# Show and clear plot again
plt.show()
plt.clf()