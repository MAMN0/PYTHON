# repeat_number = 0
# while repeat_number < 2:
#     repeat_number = int(input("Input Small Number (min 2) > "))
# #1. დაწერეთ პროგრამა, რომელის გაშვების შემდეგ კლავიატურიდან შეყვანილ ინფორმაციას ჩავწერთ data.txt ფაილში ცალ-ცალკე ხაზზე. დავასრულოთ შეტანა 0-ით.
# with open("data.txt", "a") as file_obj:
#     for i in range(repeat_number):
#         file_obj.write(f'{input("> ")} \n')
#2. დაწერეთ პროგრამა, რომლის მეშვეობით ერთი ფაილიდან წაიკითხავთ კონტენტს. ჩაწერეთ მთლიანი კონტენტი მეორე (ახალ) ფაილში ერთ ხაზზე. მითითება: თუ პირველ ფაილში არის 3 სტრიქონი, ახალ ფაილში ჩაწერეთ ერთ სტრიქონზე და გამოყავით სპეისით.
# new_text = ""
# line_count = 0
# with open("data.txt", "r") as file:
#     for i in file:
#         new_text += f'{i} '
#         print(new_text)
#     # print(file.readline())
#     print(new_text)

#3. დაწერეთ პროგრამა, დაითვლის ფაილში სიტყვების, სიმბოლოების და ხაზების რაოდენობას. დაბეჭდეთ მიღებული შედეგები.
# symbolcount = 0
# linecount = 0
# wordcount = 0
# with open("data.txt", "r") as file:
#     symbolcount = len(file.read())
# with open("data.txt", "r") as file:
#     for i in file:
#         linecount += 1
# with open("data.txt", "r") as file:
#     text = file.read()
#     for i in range(symbolcount):
#         if " " in text[i]:
#             wordcount += 1
# print(symbolcount)
# print(wordcount)
# print(linecount)
#4. შექმენით ტექსტური ფაილი რომელშიც ჩაწერთ რიცხვებს ცალ-ცალკე ხაზზე. დაწერეთ პროგრამა, რომელიც წაიკითხავს მონაცემებს ფაილიდან, აიყვანს რიცხვებს კვადრატში და ჩაწერს შედეგებს ახალ ფაილში.
# text = ""
# with open("homeworkfile.txt", "w") as file:
#     for i in range(3):
#         text += f'{input("Number > ")} \n'
#     file.write(text)
# for i in range(1, 4):
#     with open("homeworkfile.txt", "r") as file:
#         number = int(file.readline(i))
#         print(i)
#     print(number * number)
# 5. იხილეთ ატვირთული ფაილი oscars.txt, რომელშიც მოცემულია ოსკაროსანი საუკეთესო ქალის და მამაკაცის შემსრულებელი მსახიობების სია. ფაილის თითოეულ სტრიქონზე მოცემულია წელი, მსახიობის სქესი, ასაკი (ოსკარის აღების მომენტში), მსახიობის სახელი გვარი და ფილმის დასახელება. აღნიშნული ველები ერთმანეთისგან გამოყოფილია მძიმით. დაწერეთ პროგრამა, რომელიც იმუშავებს ამ ფაილთან და შეასრულებს შემდეგ დავალებებს:
#
# • მომხმარებელს შეაყვანინეთ წელი, იპოვეთ შეყვანილ წელს ოსკაროსნების სახელი
# გვარი და დაბეჭდეთ.
#
# • დაბეჭდეთ იმ მსახიობის სახელი, გვარი და ასაკი, რომელმაც ყველაზე
# ახალგაზრდამ აიღო ოსკარი.