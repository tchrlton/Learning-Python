#These 5 lines are defining the function itself and what the function is
def cheese_and_crackers(cheese_count, boxes_of_crackers):
   print("You have %d cheeses!" % cheese_count)
   print("You have %d boxes of crackers!" % boxes_of_crackers)
   print("Man that's enough for a party!")
   print("Get a blanket.\n")

def money_in_accounts(account1, account2):
   print("I have $%d dollars in my checking account." % account1)
   print("I have $%d dollars in my savings account." % account2)
   print("I have $%d dollars total." % (account1 + account2))
   print("I'm an adult now!\n")



#Replaces the arguments in the function with 20 and 30
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


#Makes new variables and then uses them as the arguments with their value
print("OR, we can use variables from out script:")
amount_of_cheese = 10
amount_of_crackers = 50

#The actual new argument using the newly made variables
cheese_and_crackers (amount_of_cheese, amount_of_crackers)

#Uses the arguments and uses the addition problems and solves it
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


'''
Uses the variables made from above and adds the corresponding number
to the function's arguments
'''
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

'''
This starts the next function
'''

#1
print("This is the amount I have in my checkings and savings account")
money_in_accounts(1037, 236)
#2
print("How much do you have in your checking and savings account?")
account1 = int(input())
account2 = int(input())

money_in_accounts(account1, account2)
#3
print("I get paid tomorrow so let's see how much I have now.")
money_in_accounts(1037 + 345, 236 + 0)
#4
print("I put 20% of my paycheck into my savings.")
money_in_accounts(1037 + (345 * .80), 236 + (345 * .20))
#5
print("I need to put some of my checkings into my savings.")
money_in_accounts(1037 - 37, 236 + 37)
#6
print("How much would your savings have with 20% taken out.")
money_in_accounts((account1 + (345 * .80)), account2 + (345 * .20))
