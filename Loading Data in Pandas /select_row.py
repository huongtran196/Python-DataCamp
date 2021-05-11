# Logical testing

print(height_inches > 70)
print(plate1 == 'FRQ123')
print(fur_color != 'brown')

# Select missing puppies

greater_than_2 = mpr[mpr.Age >2]
print(greater_than_2)
missing_dog = mpr[mpr.Status == 'Still Missing']
print(missing_dog)
not_poodle = mpr[mpr.['Dog Breed'] != 'Poodle']
print(not_poodle)

# Narrowing the list of suspects

purchase_location = credit_records[credit_records.location == 'Pet Paradise']
print(purchase_location)