"""
Your  job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""

print("Welcome to Automatica pizza order system")
size = input("What size of Pizza you want? Enter S, M, L : ")
Pepperoni = input("Do you want Pepperoni? Enter Y, N : ")
Extra_cheese = input("Do you want extra cheese? Enter Y, N : ")
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
# use try except for cases other than S,M,L
if Pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if Extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is : ${bill}")



