# 1. დაწერეთ ფუნქცია, რომელიც დაადგენს არის თუ არა პარამეტრად გადაცემული რიცხვი რაიმე მთელი რიცხვის კვადრატი. ფუნქციამ უნდა დააბრუნოს შესაბამისი მნიშვნელობა. ფუნქციის გარეთ მომხმარებელს შეატანინეთ ნებისმიერი მთელი რიცხვი. გამოიძახეთ შექმნილილ ფუნქცია ამ რიცხვისთვის და დაბეჭდეთ შესაბამისი შეტყობინება.
#
# 2. იხილეთ ატვირთული ფაილი oscars.txt, რომელშიც მოცემულია ოსკაროსანი საუკეთესო ქალის და მამაკაცის შემსრულებელი მსახიობების სია.
#
# ფაილის თითოეულ სტრიქონზე მოცემულია წელი, მსახიობის სქესი, ასაკი (ოსკარის აღების მომენტში), მსახიობის სახელი გვარი და ფილმის დასახელება. აღნიშნული ველები ერთმანეთისგან გამოყოფილია მძიმით. დაწერეთ პროგრამა, რომელიც იმუშავებს ამ ფაილთან და შეასრულებს შემდეგ დავალებებს:
#
# • მომხმარებელს შეაყვანინეთ წელი, იპოვეთ შეყვანილ წელს ოსკაროსნების სახელი
# გვარი და დაბეჭდეთ.
#
# • დაბეჭდეთ იმ მსახიობის სახელი, გვარი და ასაკი, რომელმაც ყველაზე
# ახალგაზრდამ აიღო ოსკარი.

# Root Function
def root(x):
    is_done = False
    for i in range(x):
        if i ** 2 == x:
            is_done = True
            return is_done
    if is_done == False:
        return False

Number = int(input("Enter Number > "))
print(root(Number))

# #2

#Input Year
year = input("Input Year > ")
with open("oscars.txt", "r") as oscars:
    text = oscars.read()
    i = text.find(year)
    while text[i] != ",":
        i += 1
    i += 1
    while text[i] != ",":
        i += 1
    i += 1
    while text[i] != ",":
        i += 1
    b = i
    i += 1
    while text[i] != ",":
        i += 1
    f = i
    print(text[b + 1:f])

# Youngest
with open("oscars.txt", "r") as oscars:
    i = 0
    youngest = 100000 ** 2
    Fullname = ""
    for i in oscars:
        if int(i[7:9]) < youngest:
            youngest = int(i[7:9])
            n = 6
            while i[n] != ",":
                n += 1
            n += 1
            while i[n] != ",":
                n += 1
            n += 1
            b = n
            while i[n] != ",":
                n += 1
            v = n
            Fullname = i[b:v]

    print(f'Youngest Is {Fullname} And Year {youngest}')