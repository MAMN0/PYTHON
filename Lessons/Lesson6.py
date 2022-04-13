# n = int(input("Input Number: "))
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i)
#     i += 1

n1 = int(input("Input Number: "))
n2 = int(input("Input Number: "))
high = 0
if n1 > n2:
    high = n1
else:
    high = n2
for i in range(1, high):
    if n1 % i == 0 and n2 % i ==0:
        print(i)