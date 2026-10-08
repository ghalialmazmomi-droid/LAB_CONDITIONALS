Age = int(input("Enter your Age: "))
day = input("Enter the day of the week : ")
student = input("Are you a student? (yes/no): ")


all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


if Age < 0:
    print("Invalid age")
    exit()

elif day not in all_days:
    print("Invalid day")
    exit()

if Age < 5:
    prise = 0
    print("Free , Enjoy ")

elif Age <= 12:
    prise = 6

elif Age <= 59:
    prise = 10

else:
    prise = 7

    if day == "Friday" and prise > 0:
        prise = prise + 2



if student == "yes" and prise    > 0:
    discount = prise * 20 / 100
    prise = prise - discount


    print( " Ticet prise :" , round(prise, 2) , " $")

    #MohamedAlnsafi