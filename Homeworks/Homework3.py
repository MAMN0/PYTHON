Text = "Input Number: "
Example = 1
print(Example, "Example")
Example += 1
print()
Number = input(Text)
if float(Number) > 0:
    print(float(Number), "Is Positive")
else:
    if int(Number) == 0:
        print(int(Number), "Equals To Zero")
    else:
        print(float(Number), "Is Negative")

print()
print(Example, "Example")
Example += 1
print()
Number = input(Text)
if int(Number) % 10 == 0:
    print(int(Number), "Last Number Is Zero")
else:
    print(int(Number), "Last Number Is Not Zero")
print()
print(Example, "Example")
Example += 1
print()
N1, N2 = float(input(Text)), float(input(Text))
if N1 > 10 and N2 > 10:
    print("ამ რიცხვების საშუალო არითმეტიკულია", (N1 + N2) / 2)
else:
    print("ამ რიცხვების ნამრავლია", N1 * N2)
print()
print(Example, "Example")
Example += 1
print()
N1, N2, N3 = float(input(Text)), float(input(Text)), float(input(Text))
if N1 <= N2 and N1 <= N3:
    print(N1, "Is Lower")
else:
    if N2 <= N1 and N2 <= N3:
        print(N2, "Is Lower")
    else:
        if N3 <= N1 and N3 <= N2:
            print(N3, "Is Lower")
print()
print(Example, "Example")
Example += 1
print()
Number = int(input(Text))
print(Number % 10)
print()
