# # #1. შექმენით ლექსიკონი: {0: 10, 1: 20}. დაამატეთ 2 ახალი ელემენტი და დაბეჭდეთ მიღებული ლექსიკონი. (გამოიყენეთ update მეთოდიც). წაშალეთ რომელიმე ელემენტი.
# print(1)
# my_dict = {0: 10, 1: 20}
# new_element = {3: 40}
# my_dict[2] = 30
# my_dict.update(new_element)
# my_dict.pop(3)
# print(my_dict)
# # 2. დაწერეთ პროგრამა, რომელიც შეაერთებს სამ ლექსიკონს:
# # dic1={1:10, 2:20}
# # dic2={3:30, 4:40}
# # dic3={5:50,6:60}
# print(2)
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# def funct1(x, y, n):
#     dic4 = {}
#     dic4.update(x)
#     dic4.update(y)
#     dic4.update(n)
#     return dic4
# print(funct1(dic1, dic2, dic3))
#
# # შედეგი: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# #
# # # 3. დაწერეთ პროგრამა რომელიც შეამოწმებს რომელიმე key (გასაღები) არის თუ არა ლექსიკონში: d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} და დაბეჭდეთ შესაბამისი შეტობინება. (მითითება: გამოიყენეთ in ოპერატორი).
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = int(input(">"))
# if key in d:
#     print(True)
# # 4. მოცემულია ლექსიკონი d = {'x': 10, 'y': 20, 'z': 30} დაბეჭდეთ თითოეული ელემენტის key და value შემდეგნაირად (მითითება: გამოიყენეთ for ციკლი):
# # x -> 10
# # y -> 20
# # z -> 30
# print(4)
# d = {'x': 10, 'y': 20, 'z': 30}
# n = d.keys()
# for i in n:
#     print(f'{i} -> {d[i]}')
#
# # 5. დაწერეთ პროგრამა, რომელიც შექმნის შემდეგი სახის ლექსიკონს (key არის 1-დან 10-მდე რიცხვები, ხოლო value- მათი კუბები). დაბეჭდეთ მიღებული ლექსიკონი.
# print(5)
# d = {}
# for i in range(1, 11):
#     d[i] = i**3
# print(d)
# # 6. შექმენით ცარიელი ლექსიკონი და დაამატეთ ელემენტები ფოტოზე მითითებული გამოსახულების მიხედვით. დაბეჭდეთ აღწერილი ადამიანის სახელი, გვარი, ასაკი და შვილების სახელები. (თავიდან ლექსიკონი ცარიელია და მერე თქვენ ამატებთ ფუნქციებით item ებს)
# d = {}
# # 7. გამოიყენეთ ატვირთული morsecode.txt ფაილი, რომელშიც მოცემულია მორზეს ანბანი - თითოეულ ხაზზე წარმოდგენილია ლათინური ასო ან სიმბოლო შესაბამისი მორზეს კოდებით, რომელიც ერთმანეთისგან გამოყოფილია Tab-ით - ‘\t’
# #
# # დაწერეთ პროგრამა, რომელშიც მომხარებელს შეაყვანინებთ ნებისმიერ ლათინურ ტექსტს. პროგრამამ შეყვანილი ტექსტი უნდა გადაიყვანოს მორზეს ანბანში და დაბეჭდოს შედეგი. შედეგის გამოტანის დროს თითოეული სიმბოლოს მორზეს კოდი ერთმანეთს დააშორეთ space-ით. ხოლო სიტყვებს შორის ჩასვით გამყოფი ხაზი | . პროგრამის წერისას გამოიყენეთ ლექსიკონი.
# Managing Dictionary
# morse_dict = {"Alpha": {}, "Digit": {}, "Diffirent_symbol": {}}
# with open("morsescode.txt", "r") as morse:
#     for i in morse:
#         n = i[0]
#         m = i[2:]
#         if n.isalpha():
#             morse_dict["Alpha"][n] = m
#         elif n.isdigit():
#             morse_dict["Digit"][n] = m
#         else:
#             morse_dict["Diffirent_symbol"][n] = m
# # Making program
# text = "niku .3"#input("Input Text In English Language > ")
# list1 = []
# for i in text:
#     if i in " ":
#         list1.append("|")
#     if i.isalpha():
#         for n in morse_dict["Alpha"].keys():
#             if i.upper() in n:
#                 list1.append(morse_dict["Alpha"][i.upper()])
#                 break
#     if i.isdigit():
#         for n in morse_dict["Digit"].keys():
#             if i in n:
#                 list1.append(morse_dict["Digit"][i])
#                 break
#     if not i.isalpha() and not i.isdigit():
#         for n in morse_dict["Diffirent_symbol"].keys():
#             if i in n:
#                 list1.append(morse_dict["Diffirent_symbol"][i])
#                 break
# # Formating Our Symbols
# ptext = ""
# for i in list1:
#     if "\n" in i:
#         ptext += f'{i[:-2]} '
#     else:
#         ptext += f'{i} '
# print(ptext)