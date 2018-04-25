people = 30
cars = 40
trucks = 15

#Simple boolean expression that decides if we should take the cars
if cars > people:
   print("We should take the cars.")
elif cars < people:
   print("We should not take the cars.")
else:
   print("We can't decide.")
#Decides if we should take the trucks
if trucks > cars:
   print("That's too many trucks.")
elif trucks < cars:
   print("Maybe we could take the trucks.")
else:
   print("We still can't decide.")
#The final decision on whether to take the trucks based on the people
if people > trucks:
   print("Alright, let's just take the trucks.")
else:
   print("Fine, let's stay home then.")
#Complex boolean expression to see what it outputs with quick tests.
if cars > people or trucks < cars:
   print("We should take the cars and the trucks.")
elif (cars * 2) == people and trucks > cars:
   print("Don't take the trucks.")
else:
   print("We are not going!")
