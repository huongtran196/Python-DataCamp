# Creating line plot

import matplotlib.pyplot as plt

plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

plt.title('Officer Work Hours')
plt.xlabel('Day of Week')
plt.ylabel('Hours Worked')
plt.text(2.5, 80, 'Missing June data')

plt.legend()
plt.show()

# Tracking crime statistics

print(plt.style.available)
plt.style.use('fivethirtyeight')

plt.plot(data.['Year'], data.['Phoenix Police Dept'], label='Phoenix', color='DarkCyan')
plt.plot(data.['Year'], data.['Los Angeles Police Dept'], label='Los Angeles', linestyle=':')
plt.plot(data.['Year'], data.['Philadelphia Police Dept'], label='Philadelphia', marker='s')

plt.legend()
plt.show()

# Identifying kidnapper

plt.plot(ransom.letter, ransom.frequency, label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

plt.xlabel('Letter')
plt.ylabel('Frequency')

plt.legend()
plt.show()

