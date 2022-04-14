text = "Input Number: "
example = 1
print(example, "Example")
example += 1
print()
# 1. შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უდიდესი საერთო გამყოფი.
n1 = int(input(text))
n2 = int(input(text))
low = n1
n = 0
if n2 < n1:
    low = n2
for i in range(1, low + 1):
    if n1 % i == 0 and n2 % i == 0:
        if i > n:
            n = i
print(n)
input()
print()
print(example, "Example")
example += 1
print()
# 2. შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.
n = 0
n1 = int(input(text))
n2 = int(input(text))
low = n1
if n2 < n1:
    low = n2
for i in range(2, low + 1):
    if n1 % i == 0 and n2 % i == 0:
        n = i
        break
if int(n) == 0:
    print("NO RESULT")
print(n)
input()
print()
print(example, "Example")
example += 1
print()
# 3. შეიყვანეთ 10 რიცხვი ციკლის გამოყენებით. იპოვეთ რიცხვებს შორის უდიდესი კენტი
# რიცხვი და დაბეჭდეთ. თუ კენტი რიცხვი არ შეგხვდათ, გამოიტანეთ შესაბამისი შეტყობინება.
h = 0
n = int(input(text))
if n % 2 != 0:
    h = n
for i in range(9):
    n = int(input(text))
    if n % 2 != 0:
        if n <= h:
            h = n
print(h)