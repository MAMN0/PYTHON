text = "Input Number: "
example = 1
print(example, "Example")
example += 1
print()
# # 1. დაბეჭდეთ 2-დან 1000-მდე ყველა მარტივი რიცხვი.
# is_prime = False
# n = 2
#
#     if n % m == 0:
#         is_prime = True
#     if is_prime:
#         continue
#     else:
#         print(n)
#     n += 1
print()
print(example, "Example")
example += 1
print()
n1 = 1
n2 = 1
print(n1)
print(n2)
for i in range(0, 101):
    n2 += n1
    if n2 > 100:
        break
    print(n2)
    n1 += n2
    if n1 > 100:
        break
    print(n1)

# print()
# print(example, "Example")
# example += 1
# print()
# # 3. შეიყვანეთ ნებისმიერი რიცხვი. იპოვეთ ამ რიცხვის ციფრთა რაოდენობა და დაბეჭდეთ. (len ფუნქციის გარეშე)
# n = int(input(text))
# m = 0
# d = 0
# k = 0
# for i in range(1, n):
#     m = n % 10
#     d = (n // 10) % 10
#     k = (n // 10) - d
#     print(m, d, k)
#     break
# print(example, "Example")
# example += 1
# print()
# #
# #
# print(example, "Example")
# example += 1
# print()
# #
# #
# print()
# print(example, "Example")
# example += 1
# print()
# t = str(input())
