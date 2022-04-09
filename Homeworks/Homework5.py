example = 1
print((example, "Example"))
example += 1
print()
#  დაბეჭდეთ 5-ის ჯერადი რიცხვები 20-დან 125-ის ჩათვლით.
# i = 20
# while i < 126:
#     if i % 5 == 0:
#         print(i)
#     i += 1
for i in range(20, 126):
    if i % 5 == 0:
        print(i)
print()
print(example, "Example")
example += 1
print()
# დაბეჭდეთ 8-ის ჯერადი რიცხვები 200-დან 25-ის ჩათვლით კლებადობით.
# i = 200
# while i > 25:
#     if i % 8 == 0:
#         print(i)
#     i += 1
for i in range(200, 25, -1):
    if i % 8 == 0:
        print(i)
print()
print(example, "Example")
example += 1
print()
#  დაბეჭდეთ 1500-დან 2100-ის ჩათვლით რიცხვები,
#  რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად.
i = 1500
# while i < 2101:
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)
#     i += 1
for i in range(1500, 2101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
print()
print(example, "Example")
example += 1
print()
# დაითვალეთ 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი,
# რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად. დაბეჭდეთ მიღებული შედეგი.

# i = 1500
# res = 0
# while i < 2101:
#     if i % 5 == 0 and i % 7 == 0:
#         res = res + i
#     i += 1
# print(res)
res = 0
for i in range (1500, 2101):
    if i % 5 == 0 and i % 7 == 0:
        res = res + i
print(res)
print()
print(example, "Example")
example += 1
print()
# დაითვალეთ 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის
# ჯერადი ერთდროულად. როგორც კი რიცხვების ჯამი გადააჭარბებს 20 000-ს,
# შეწყვიტეთ ციკლი. დაბეჭდეთ მიღებული ჯამი ეკრანზე.
# i = 1500
# res = 0
# while i < 2101:
#     if i % 5 == 0 and i % 7 == 0:
#         res = res + i
#     if res > 20000:
#         break
#     i += 1
# print(res)
res = 0
for i in range(1500, 2101):
    if i % 5 == 0 and i % 7 == 0:
        res = res + i
    if res > 20000:
        break
        i += 1
print(res)
print()
print(example, "Example")
example += 1
print()
# დაითვალეთ 1500-დან 2100-ის ჩათვლით
# 5-ის ჯერადი რიცხვების რაოდენობა. დაბეჭდეთ შედეგი.
# i = 1500
# n = 0
# while i < 2100:
#     if i % 5 == 0:
#         n += 1
#     i += 1
# print(n)
n = 0
for i in range(1500, 2100):
    if i % 5 == 0:
        n += 1
print(n)
print()
print(example, "Example")
example += 1
print()
# შეიყვანეთ 10 რიცხვი კლავიატურიდან
# ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო არითმეტიკული.
# n = 0
# i = 0
# while i < 10:
#     n = n + int(input("Input Number: "))
#     i += 1
# print(n / 10)
n = 0
for i in range(1, 11):
    n = n + int(input("Input Number: "))
print(n / 10)
print()
print(example, "Example")
example += 1
print()
# დაითვალეთ 1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი და დაბეჭდეთ შედეგი.
# i = 1
# n = 0
# while i < 100:
#     if i % 2 == 0:
#         n += i
#     i += 1
# print(n)
n = 0
for i in range(1, 100):
    if i % 2 == 0:
        n += i
    i += 1
print(n)
print()
print(example, "Example")
example += 1
print()
for i in range(15, 150):
    if i == 50 or i == 75 or i == 80:
        continue
    else:
        print(i)
print()
print(example, "Example")
example += 1
print()
n = int(input("Input Number: "))
i = 1
m = 1
while i < (n + 1):
    m *= i
    print(m)
    i += 1
print(m)