cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#this is 100-30
cars_not_driven = cars - drivers
#this is 30
cars_driven = drivers
#this is 30*4.0
carpool_capacity = cars_driven * space_in_a_car
#this is 90 divided by 30
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", int(average_passengers_per_car), "in each car.")


#the reason car_pool_capactity does not get identified is bc its a different
#variable than carpool_capacity. It is seen as a different variableself.

#4.0 is better than 4 since its more accurate and has more room in case the
#remainder is a fraction
