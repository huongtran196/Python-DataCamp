import matplotlib.pyplot as plt
print(cellphone.head(5))

plt.scatter(cellphone.x, cellphone.y, color='red', market='s', alpha=0.1)
plt.ylabel('Longitude')
plt.ylabel('Latitude')

plt.show()

plt.scatter(gpd_cap, life_exp)
plt.xscale('log')

plt.show()

plt.scatter(pop, life_exp)
plt.show()

import numpy as np
np_pop = np.array(pop)
np_pop = np_pop * 2

plt.scatter(gdp_cap, life_exp, s = np_pop, c = col, alpha = 0.8)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')

# Add title
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# After customizing, display the plot
plt.show()
