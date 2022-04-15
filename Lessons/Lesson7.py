text = "Input Number: "
n = int(input(text))
h = 0
for i in range(2, n):
    if n % i == 0:
        h = 1
if h == 1:
    print("-")
else:
    print("+")

