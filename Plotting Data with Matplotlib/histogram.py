# Create a histogram of the column 'weight' from the DataFrame 'puppies'
import matplotlib.pyplot as plt
plt.hist(puppies.weight)

# Change the number of bins to 50 and range from 5 to 35
plt.hist(puppies.weight, bins=50, range= (5,35))

# Add label
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()