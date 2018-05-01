states = {
   'Tennessee': 'TN',
   'Alabama': 'AL',
   'Mississippi': 'MS',
   'Virginia': 'VA',
   'Kentucky': 'KY'
}

cities = {
   'KY': 'Frankfurt',
   'AL': 'Montgomery',
   'TN': 'Nashville'
}

cities['VA'] = 'Richmond'
cities['MS'] = 'Jackson'


print('-' * 10)
print("TN State has: ", cities['TN'])
print("MS State has: ", cities['MS'])

print('-' * 10)
print("Alabama's abbreviation is: ", states['Alabama'])
print("Kentucky's abbreviation is: ", states['Kentucky'])

print('-' * 10)
print("Tennessee has: ", cities[states['Tennessee']])
print("Virginia has: ", cities[states['Virginia']])

print('-' * 10)
for state, abbrev in states.items():
   print("%s is abbreviated %s" % (state, abbrev))

print('-' * 10)
for abbrev, city in cities.items():
   print("%s has the city %s" % (abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
   print("%s state is abbreviated %s and has city %s" % (
      state, abbrev, cities[abbrev]))

# this sorts the string alphabetically
print('-' * 10)
for state, abbrev in sorted(states.items()):
   print("%s is abbreviated %s" % (state, abbrev))
