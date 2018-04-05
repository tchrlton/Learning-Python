#10 is being formatted into this string
x = "There are %d types of people." % 10
#simple variable
binary = "binary"
#simple variable
do_not = "don't"
#list of strings inside of the string
y = "Those who know %s and those who %s." % (binary, do_not)

#This line is printing out  the x variable from above
print(x)
#This line is prnting out the y variable from above
print(y)

#This prints out the exact output of variable x because of %r
print("I said: %r." % x)
#Lists out the variable of y, which inludes two other variables
print("I also said: '%s'." % y)

#simple variabl
hilarious = False
#variable that can be put into another variable
joke_evaluation = "Isn't that joke so funny?! %r"
#prints out variable hilarious no matter what
print(joke_evaluation % hilarious)

#simple string
w = "This is the left side of..."
#simple string
e = "a string with a right side."

#will print out both w + e to make a complete sentence.
#two strings added togehter puts them together in one long string.
print(w + e)
