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
