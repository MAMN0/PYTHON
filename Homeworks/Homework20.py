#1. შექმენით სია fruits, რომელის ელემენტებია: Watermelon, Banana, Apple. დაალაგეთ ლისტის ელემენტები ალფაბეტის უკუ-მიმართულებით და დაბეჭდეთ ისინი.

#2. შექმენით ფაილი data_numbers.txt იმავე დირექტორიაში სადაც py ფაილია მოთავსებული, ჩაწერთ მასში თქვენთვის სასურველ რიცხვები ცალ-ცალკე ხაზზე. დაწერეთ პროგრამა, რომლის მეშვეობით წაიკითხავთ მონაცემებს ფაილიდან და რიცხვებს მოათავსებთ ლისტის ელემენეტებად. წარმოადგინეთ ლისტი რიცხვითი ელემენტების (და არა სტრიქონების) სახით.

#3. შექმენით ლისტი რიცხვითი ელემენტებით. shuffle ფუნქციის გამოყენებით (random მოდულიდან) მოახდინეთ ლისტის ელემენტების შემთხვევითად არევა და დაბეჭდეთ მიღებული ლისტი.(მითითება: ფუნქცია იწერება შემდეგნაირად: random.shuffle(x) სადაც x ლისტის დასახელებაა)

#4. შექმენით ლისტი რიცხვითი მნიშვნელობებით. რანდმულად ამოარჩიეთ ლისტის რომელიმე ელემენტი და დაბეჭდეთ. (მითითება: წინა სავარჯიშოს მსგავსად გამოიყენეთ random მოდულის choice ფუნქცია).

#5. დაწერეთ პროგრამა, რომელშიც შეიტანთ (input-ით) ნებისმიერ დიდ რიცხვს (მაგ. 342387410984). იპოვეთ რიცხვის ციფრთა ჯამი. (მითითება: თავდაპირველად გარდაქმენით რიცხვი ლისტად).

#6. იპოვეთ ლისტში [1, 5, 23, 5, 12, 2, 5, 1, 18, 5] ყველაზე ხშირად განმეორებადი რიცხვი. დაბეჭდეთ შედეგი. ასევე მიუთითეთ რამდენჯერ შეგხვდათ ლისტში ყველაზე ხშირად განმეორებადი რიცხვი.

#7. შექმენით ლისტი ც. პროგრამის გაშვების შემდეგ მომხამრებელმა შეიყვანოს (input) ნებისმიერი ფაილის დასახელება. თუ ფაილის გაფართოება ემთხევა ლისტის რომელიმე ელემენტს, დაბეჭდოს ეკრანზე “Yes”, წინააღმდეგ შემთხვავაში დაბეჭდოს “No”.

#8. სტრიქონი 'python php pascal javascript java c++' წარმოადგინეთ ლისტის სახით (სტრიქონის თითოეული სიტყვა ლისტის თითოეული ელემენტად). იპოვეთ ლისტის ყველაზე გრძელი ელემენტი (ანუ ყველაზე გრძელი სიტყვა).

#9. (ლისტების გამოყენებით) იხილეთ ატვირთული ფაილი oscars.txt, რომელშიც მოცემულია ოსკაროსანი საუკეთესო ქალის და მამაკაცის შემსრულებელი მსახიობების სია (შეასრულეთ დავალება სიების გამოყენებით).

#ფაილის თითოეულ სტრიქონზე მოცემულია წელი, მსახიობის სქესი, ასაკი (ოსკარის აღების მომენტში), მსახიობის სახელი გვარი და ფილმის დასახელება. აღნიშნული ველები ერთმანეთისგან გამოყოფილია მძიმით. დაწერეთ პროგრამა, რომელიც იმუშავებს ამ ფაილთან და შეასრულებს შემდეგ დავალებებს:

#• მომხმარებელს შეაყვანინეთ წელი, იპოვეთ შეყვანილ წელს ოსკაროსნების სახელი გვარი და დაბეჭდეთ.
#• დაბეჭდეთ იმ მსახიობის სახელი, გვარი და ასაკი, რომელმაც ყველაზე ახალგაზრდამ აიღო ოსკარი.

# Resources
# import random
#
# # 1
#
# fruits = ['Watermelon', 'Banana', "Apple"]
# fruits.reverse()
# print(fruits)
#
# # 2
#
# list = []
# with open('data_numbers.txt', "r") as data:
#     for i in data:
#         list.append(int(i))
# print(list)
# print()
#
# # 3
#
# list = []
# for i in range(5):
#     list.append(random.randint(1, 100))
# print(list)
# random.shuffle(list)
# print(list)
# print()
#
# # 4
#
# list = []
# for i in range(5):
#     list.append(random.randint(1, 100))
# print(list)
# print(random.choice(list))
# print()
#
# # 5
#
# sum = 0
# while True:
#     number = input("Input Big Number (Example 342387410984, lenght must be min 8) > ")
#     if len(number) >= 8:
#         break
# list = [int(number)]
# print(list)
# for i in number:
#     sum += int(i)
# print(sum)
# print()

# 6

# countlist = []
# symbollist = []
# lasti= ""
# list = [1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
# for i in list:
#     countv = 0
#     if str(i) in lasti:
#         continue
#     for n in list:
#         if i == n:
#             countv += 1
#             lasti += str(i)
#     symbollist.append(i)
#     countlist.append(countv)
# print(countlist)
# print(symbollist)
# h = countlist.index(max(countlist))
# print(symbollist[h])

# 7

# extensions = ['txt', 'jpg', 'gif', 'html']
# while True:
#     file = input("Input Your File Name And File Expansion > ")
#     if "." in file:
#         break
# contains = False
# for i in extensions:
#     if i in file:
#         contains = True
#         break
#     else:
#         contains = False
# print(contains)

# 8

# text = 'python php pascal javascript java c++'
# list = text.split()
# print(list)
# lenght = 0
# index = ""
# for i in list:
#     if len(i) > lenght:
#         lenght = len(i)
#         index = i
# print(index)

# 9

