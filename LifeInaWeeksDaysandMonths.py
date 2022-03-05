# To Calculate no of days weeks and months you have left if you live for 90 years
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

age = int(input("what is your age ? "))

Years_passed = age
Days_passed = 365 * Years_passed
Weeks_passed = 52 * Years_passed
Months_passed = 12 * Years_passed

message = f"Your age is {Years_passed}, Months passed {Months_passed}, Weeks passed {Weeks_passed}, Days passed {Days_passed}"
print(message)

Days_left = 90*365 - Days_passed
# print(f"No of days left : {Days_left}")
Weeks_left = 90*52 - Weeks_passed
# print(f"No of weeks left : {Weeks_left}")
Months_left = 90*12 - Months_passed
#print(f"No of months left : {Months_left}")
Years_left = 90-Years_passed
#print(f"No of years left : {Years_left}")

Reality_check = f" You have {Years_left} Years left, {Months_left} Months left, {Weeks_left} weeks left and {Days_left} Days left"
print(Reality_check)
