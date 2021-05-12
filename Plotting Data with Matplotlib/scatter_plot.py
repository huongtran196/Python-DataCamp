import matplotlib.pyplot as plt
print(cellphone.head(5))

plt.scatter(cellphone.x, cellphone.y, color='red', market='s', alpha=0.1)
plt.ylabel('Longitude')
plt.ylabel('Latitude')

plt.show()