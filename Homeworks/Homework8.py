text = "Input Number: "
example = 1
# print(example, "Example")
# example += 1
# print()
# # 1. შეიყვანეთ ნებისმიერი რიცხვი. დაადგინეთ არის თუ არა
# # შეტანილი რიცხვი პალინდრომი. (მითითება: პალინდრომია რიცხვი, რომელიც მარჯვნიდან და მარცხნიდან ერთნაირად იკითხება). მაგ. 12521 არის პალინდრომი
# # ჯერჯერობით არ გავაკეთებ
# number = int(input(text))
# temp_number = number
# first_number_sum = 0
# second_number_sum = 0
# count = 0
# legnth_count = 0
# mirror_first_number = 0
# mirror_second_number = 0
#
# while temp_number >= 1:
#     count += 1
#     temp_number /= 10
# # print(count)
#
# if count % 2 != 0:
#     legnth_count = (count - 1) / 2
# else:
#     legnth_count = count / 2
#
# # print(legnth_count)
#
# temp_number = number
# for i in range(1, int(legnth_count + 1)):
#     first_number_sum *= 10
#     first_number_sum += temp_number % 10
#
#     temp_number //= 10
# print(first_number_sum)
#
# temp_number = first_number_sum
# while temp_number > 1:
#     mirror_first_number *= 10
#     mirror_first_number += temp_number % 10
#
#     temp_number //= 10
# #
# # print(mirror_first_number)
#
# temp_number = number
# while temp_number > 1:
#     second_number_sum *= 10
#     second_number_sum += temp_number % 10
#
#     temp_number //= 10
#
# print(second_number_sum)
# print()
# temp_number = second_number_sum
# while temp_number > 1:
#     mirror_second_number *= 10
#     mirror_second_number += temp_number % 10
#
#     temp_number //= 10
#
# print(mirror_second_number)





print()
print(example, "Example")
example += 1
print()
# 2. შეიყვანეთ ორი რიცხვი. დაბეჭდეთ ამ ორ რიცხვს შორის არსებული ყველა „სარკისებური მარტივი“ რიცხვები
# (Mirror Prime Numbers). რიცხვი „სარკისებურად მარტივია“ თუ იგი არის მარტივი და მისი შებრუნებული მნიშვნელობაც მარტივია.
number1 = int(input(text))
number2 = int(input(text))
temp_number = 0
mirror_prime_number = 0
is_mirror_number_prime = False

for i in range(number1 + 1, number2):
    temp_number = i
    while temp_number > 1:
        mirror_prime_number *= 10
        mirror_prime_number += temp_number % 10
        temp_number /= 10
    for n in range(2, int(miror_prime_number)):
        if mirror_prime_number % n:
            break
        else:
            print(mirror_prime_number)