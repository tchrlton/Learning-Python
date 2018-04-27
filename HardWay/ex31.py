print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
   print("There's a giant bear here eating a cheese cake. What do you do?")
   print("1. Take the cake.")
   print("2. Scream at the bear.")

   bear = input("> ")

   if bear == "1":
      print("the bear eats your face off. Good job!")
   elif bear == "2":
      print("The bear eats your legs off. Good job!")

      kill = input("> ")

      if kill == "1":
         print("You find a knife.")

         knife = input("> ")

         if knife == "1":
            print("You throw the knife and it lands in the middle of the bear's eyes.")
         elif knife == "2":
            print("You slash the legs of the bear causing the bear to run away. ")
         else:
            print("You do nothing and get ripped apart by the bear.")

      elif kill == "2":
         print("You find a gun.")

         gun = input("> ")

         if gun == "1":
            print("You shoot the bear in the head twice, killing the bear.")
         elif gun == "2":
            print("You shoot the bear in the knee, ruining his career in the circus.")
         else:
            print("You go to grab the gun, you miss, and then get ripped apart.")

      else:
         print("You bleed out and die!")
   else:
      print("Well, doing %s is probably better. Bear runs away." % bear)



elif door == "2":

   print("You stare into the endless abyss at Cthulhu's retina.")
   print("1. Blueberries.")
   print("2. Yellow jacket clothespins.")
   print("3. Understanding revolvers yelling melodies.")

   insanity = input("> ")

   if insanity == "1" or insanity == "2":
      print("Your body survives powered by a mind of jello. Good job!")
   elif insanity == "3":
      print("Your bones crumble making your body into a sack of potatoes.")
   else:
      print("The insanity rots your eyes into a pool of muck. Good job!")

else:
   print("You stumble around and fall on a knife and die. Good job!")
