#Changing these values will change the output depending on what they are
people = 17
cats = 19
dogs = 5

#Every line under each if statement needs to be indented by 4 spaces to show
#the it is enclosed in that if-then statement.
if people < cats:
  print("Too many cats! The world is doomed!")

if people > cats:
   print("Not many cats! The world is saved!")
#Added the != instead of < to see what happened.
if people != dogs:
   print("The world is drooled on!")

if people > dogs:
   print("The world is dry!")


dogs += 5

if people >= dogs:
   print("People are greater than or equal to dogs.")

if people <= dogs:
   print("People are less than or equal to dogs.")


if people == dogs:
   print("People are dogs.")
