year = int(input("Input year: "))

if not year % 4 == 0:
    print(year, "Is not Nakiani")
elif not year % 100 == 0:
    print((year, "Is Nakiani"))
elif not year % 400 == 0:
    print(year, "Is Not Nakiani")
else:
    print(year, "Is Nakiani")