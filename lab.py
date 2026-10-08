Their_age: int = int (input("Enter your Age"))
Day_of_the_week:str=input("Enter The Day")
Are_You_Student:str=input("Are You Student")

price=0


if (Day_of_the_week != "Monday" and
    Day_of_the_week != "Tuesday" and
    Day_of_the_week != "Wednesday" and
    Day_of_the_week != "Thursday" and
    Day_of_the_week != "Friday" and
    Day_of_the_week != "Saturday" and
    Day_of_the_week != "Sunday"):
    print("Invalid day")

if Their_age < 0:
    print("Invalid age")

if Their_age <= 5:
    print("free")
else:
    if Their_age <=12:
      price = 6
    elif Their_age <=59:
      price = 10
    else:
     price = 7

    if Day_of_the_week == "Friday":
     price = price + 2

    if Are_You_Student =="yes":
     price = price * 0.80

    print(f"Ticket price:${price:.2f}")