#Load a DataFrame
import pandas as pd
import matplotlib.pyplot as plt
r = pd.read_csv('ransom.csv')
print(r)
plt.plot(letters,frequency)
plt.show()

#Snooping for suspects
plate = 'FRQ****'
lookup_plate('FRQ****')
lookup_plate(plate, color='Green')