# Display DataFrame hours using print command
print(hours)

# Create a bar chart of the column avg_hours_worked for each officer from the DataFrame hours
plt.bar(hours.officer, hours.avg_hours_worked, yerr=hours.std_hours_worked)
plt.show()

# Create a stacked bar chart of the time each officer spends on desk_work and field_work. Label as "Desk Work" and "Field Work"
plt.bar(hours.officer, hours.desk_work, label="Desk Work")
plt.bar(hours.officer, hours.field_work, bottom=hours.desk_work, label="Field Work")

plt.legend()
plt.show()

