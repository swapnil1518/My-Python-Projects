year = int(input("enter a year you want to check? "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("leap year")
        else:
            print("not leap year")
    else:
        print(" leap year")
else:
    print("not leap year")


# leap year if perfectly divisible by 400

# not a leap year if divisible by 100 , but not divisible by 400

#leap year if not divisible by 100, but divisible by 4