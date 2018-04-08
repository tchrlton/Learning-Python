#this is the variable that will be used throught the lines of code
formatter = "%r %r %r %r"

#uses %r to print out whats in parantheses in its raw format
print(formatter % (1, 2, 3, 4))
#uses %r to print the individual strings in order.
#the "" will turn into '' quotes bc they are shorter strings?
print(formatter % ("one", "two", "three", "four"))
#uses %r to print out whats in the parentheses in its raw format
print(formatter % (True, False, False, True))
#use %r to print out the raw format of the variable
print(formatter % (formatter, formatter, formatter, formatter))
#uses %r to print each string out, in order, in its raw format
#python will run efficently so one of these lines could have singe quotes
print(formatter % (
   "I had this thing.",
   "That you could type up right.",
   "But it didn't sing.",
   "So I said goodnight."
))
