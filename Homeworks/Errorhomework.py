# import random
#
#
# # 1
# def errorexpector1(a, b):
#     while True:
#         try:
#             c = a / b
#             print(c)
#         except ValueError:
#             print('Input Only Integer')
#             continue
#         except ZeroDivisionError:
#             print('Can not be divided by zero!')
#             continue
#         break
#
# # 2
# def errorexpector2(a, b):
#     try:
#         c = a % b == 0
#         if c:
#             return a / b
#     except ValueError:
#         print('Input Only Integer')
#     except ZeroDivisionError:
#         print('Can not be divided by zero!')
#
#
# # 3
# def errorexpector3():
#     try:
#         list1 = [random.randint(1,10), random.randint(1,10), random.randint(1,10)]
#         print("Hallo i am Jarvis and i have list which's length is 3")
#         answer = int(input("Input which index do you want to see"))
#         print(list1[answer])
#     except IndexError:
#         print(answer, "Does not exist")
#     except ValueError:
#         print('Input Only Integer')
# print(errorexpector3())

# def errorexpector4():
#     try:
#         with open("myresult.txt", "r") as myresult:
#             print(myresult.read())
#     except FileNotFoundError:
#         print("I Can't Find That File")
# errorexpector4()