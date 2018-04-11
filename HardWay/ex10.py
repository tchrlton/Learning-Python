#\t is used to tab the string in the terminal
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

#Put \b to see what what is actually does into line 9
fat_cat = '''
I'll do a list:
\t* Cat  \bFood
\t* \'Fishies\'
\t* Catnip\n\t* Grass
'''

"""
Using %r would make it show all of the backslashes (\), so use %s instead.
I added the %s format even though it does the same thing to get some self-
practice inself.
"""
print("%s" % tabby_cat)
print("%s" % persian_cat)
print("%s" % backslash_cat)
print("%s" % fat_cat)


"""
Keeps printing i for infinity while its True, also uses \r for carriage return
which overwrites the beginning of the statement with whatever is after \r
"""

"""
while True:
   for i in ["/","-","|","\\","|"]:
      print("%s\r" % i,)
"""

Mom = "Mom: Milk, Bread, Cheese"
Sister = "Sister: \'Makeup\', Juice, and Soda"
Brother = "Brother: Glue, Redbox, and Redbull"

Me_Myself_and_I = "Me:\tMillion Dollars\n\tA Life\n\tGaming Pc"

print("Dad: What did everyone want from the grocery store?")
print(Mom)
print(Sister)
print(Brother)
print(Me_Myself_and_I)
print("Dad: .....")
