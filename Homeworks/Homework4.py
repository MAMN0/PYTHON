year = int(input("Input year: "))

if not year % 4 == 0:
    print(year, "Is not Leap")
elif not year % 100 == 0:
    print(year, "Is Leap")
elif not year % 400 == 0:
    print(year, "Is Not Leap")
else:
    print(year, "Is Leap")