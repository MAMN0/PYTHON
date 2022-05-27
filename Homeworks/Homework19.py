# 1. შექმენით ლისტი numbs ნებისმიერ 5 რიცხვითი მნიშვნელობით. იპოვეთ ამ რიცხვების ჯამი, მინიმალური, მაქსიმალური და საშუალო არითმეტიკული. ასევე შეასრულეთ შემდეგი ოპერაციები:
# • სიას დაამატეთ ბოლო ელემენტად რიცხვი 102
# • სიის მესამე ელემენტად ჩასვით რიცხვი 205
# • წაშალეთ სიის მე-4 ელემენტი
# • დაალაგეთ სია ზრდადობის მიხედვით და დაბეჭდეთ
#
# 2. დაწერეთ პროგრამა, რომლის მეშვეობით შეიყვანთ (input-ით) 10 მონაცემს. წარმოადგინეთ და დაბეჭდეთ ისინი ლისტის ელემენტების სახის.
#
# 3. დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა ლისტი, დაითვლის ლისტის ელემენტების ნამრავლს და დააბრუნებს შედეგს. გამოიძახეთ ფუნქცია ნებისმიერი სიისთვის.
#
# 4. დაწერეთ პროგრამა, რომელიც რიცხვითი მნიშვნელობების ლისტში ამოშლის კენტ რიცხვებს. დაბეჭდეთ მიღებული ლისტი.
#
# 5. შექმენით 5 ელემენტიანი ლისტი (რიცხვითი მნიშვნელობებით). თითოეული ელემენტი გაზარდეთ 10-ით და დაბეჭდეთ ლისტი.
#
# 6. შექმენით 10 ელემენტიანი ლისტი, რომლის ელემენტებია ნებისმიერი შემთხვევითი მთელი რიცხვები 25-დან 110-მდე. დაბეჭდეთ ლისტი და იპოვეთ მინიმალური ელემენტი.
#

# 7. დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა 2 ლისტი. ფუნქცია აბრუნებს მნიშვნელობა True-ს თუ ლისტებს აქვთ ერთი მაინც საერთო ელემენტი. წინააღმდეგ შემთხვევაში აბრუნებს False მნიშვნელობას.

# 1
# import random
# Numbs = []
# normal_a = 1
# lowest = 1000
# greatest = 0
# for i in range(5):
#     Numbs.append(random.randint(1, 100))
# print(Numbs)
# normal_a /= len(Numbs)
# Numbs.append(102)
# Numbs.insert(3, 205)
# Numbs.pop(4)
# numbs = []
# previus_num= 0
# for i in Numbs:
#     normal_a += i
#     if i < lowest:
#         lowest = i
#     if i > greatest:
#         greatest = i
# normal_a /= len(Numbs)
# for i in range(len(Numbs)):
#     for n in range(i + 1, len(Numbs)):
#         if Numbs[i] > Numbs[n]:
#             temp = Numbs[i]
#             Numbs[i] = Numbs[n]
#             Numbs[n] = temp
# print(Numbs)
# print(lowest)
# print(greatest)
# print(normal_a)

# # 2
# my_list = []
# for i in range(10):
#     my_list.append(input("> "))
# print(my_list)

# 3

# def Multiplied_list(x):
#     Multiplied = 1
#     for i in x:
#         Multiplied *= i
#     return Multiplied
# my_list = []
# for i in range(random.randint(4, 10)):
#     my_list.append(random.randint(1, 10))
# print(my_list)
# print(Multiplied_list(my_list))

# 4

# my_list = []
# for i in range(random.randint(4, 10)):
#     my_list.append(random.randint(1, 10))
# print(my_list)
# list = []
# for i in my_list:
#     if i % 2 == 0:
#         list.append(i)
# my_list = list
#
# print(my_list)

# 5
# my_list = []
# for i in range(5):
#      my_list.append(random.randint(1, 100))
# print(my_list)
# for i in my_list:
#     my_list[my_list.index(i)] = i * 10
# print(my_list)

# 6

# list = []
# for i in range(10):
#     list.append(random.randint(25, 109))
# youngest = 110
# for i in list:
#     if i < youngest:
#         youngest = i
# print(list)
# print(youngest)

# 7
# list1 = []
# list2 = []
# for i in range(random.randint(5, 10)):
#     list1.append(random.randint(1, 20))
#     list2.append(random.randint(1, 20))
# print(list1)
# print(list2)
# def contain_mutual_numb(x, y):
#     for i in x:
#         for n in y:
#             if i == n:
#                 return True
#     return False
# print(contain_mutual_numb(list1, list2))