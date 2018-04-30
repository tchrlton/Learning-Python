'''
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")
#
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
#removes and returns the last item on the list more_stuff until there are 10
while len(stuff) != 10:
   #pop(more_stuff)
   next_one = more_stuff.pop()
   print("Adding: ", next_one)
   #append(stuff, next_one)
   stuff.append(next_one)
   print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-2])
print(stuff.pop)
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
'''

things = "Phone Laptop Beats Backpack Car Chair Mouse Monitor TV Dog"

print("I want every other item in the list!")

stuff = things.split(' ')
more_stuff = ["Bed", "Dresser", "Table"]

while len(stuff) != 13:
   next_one = more_stuff.pop()
   print("Adding: ", next_one)
   stuff.append(next_one)
   print("There are %d items now." % len(stuff))

print("There we go: " )
print(stuff[0::2])
