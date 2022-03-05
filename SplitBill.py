bill = float(input("what is the total Bill : "))
tip = int(input("what percentage of tip you want to give ? 10/15/20 : "))
people = int(input("How many people to split the bill ? : "))

total_bill = bill+bill*tip/100
print(f"Total bill after adding tip is : {total_bill}")
distribution = total_bill/people
final_pay = round(distribution,2)
print(f"each person has to pay : {final_pay}")