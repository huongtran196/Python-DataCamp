#Load a DataFrame
import pandas as pd
r = pd.read_csv('ransom.csv')
print(r)
plt.plot(x_values,y_values)
plt.show()

#Snooping for suspects
plate = 'FRQ****'
lookup_plate('FRQ****')
lookup_plate(plate, color='Green')