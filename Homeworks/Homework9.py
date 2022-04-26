# 1. შეიტანეთ ათწილადი რიცხვი, დაამრგვალეთ ათწილად ნაწილში მეათედის სიზუსტით (1 ციფრი ათწილად ნაწილში) და დაბეჭდეთ შედეგი.
# გამოიყენეთ round, ceil, floor, trunc ფუნქციები სათითაოდ და შეამოწმეთ შედეგი თითოეულის გამოყენებით.
text1 = ("Input Float Number: ")
text2 = ("Input Number: ")
example = 1
print(example, "Example")
example += 1
print()
from math import ceil, floor, trunc
Number = float(input(text1))
print("round()", round(Number, 1))
print()
print("ceil()", ceil(Number))
print()
print("floor()", floor(Number))
print()
print("trunc()", trunc(Number))
print()

#2. შეიტანეთ სამი რიცხვი, იპოვეთ მათ შორის მაქსიმუმი და დაბეჭდეთ შედეგი. გამოიყენეთ max ფუნქცია.

print(example, "Example")
example += 1
print()
Number1 = int(input(text2))
Number2 = int(input(text2))
Number3 = int(input(text2))
print()
print("Most Greatest is", max(Number1, Number2, Number3))
print()
print()

# 3. გამოთვალეთ 3 ხარისხად 8 ფუნქციის გამოყენებით და დაბეჭდეთ შედეგი. ასევე გამოთვალეთ 2 ხარისხად 9, 4 ხარისხად 6 და დაბეჭდეთ მიღებული შედეგი.
print(example, "Example")
example += 1
print()
print(pow(3, 8), pow(2, 9), pow(4, 6))


# 4. გამოთვალეთ მათემატიკური ფუნქციის გამოყენებით: ა) კვადრატული ფესვი 225625-დან ბ) კვადრატული ფესვი 4225-დან
print()
print(example, "Example")
example += 1
print()
print("ა) კვადრატული ფესვი 225625-დან")
from math import sqrt
print(sqrt(225625))
print()
print("ბ) კვადრატული ფესვი 4225-დან")
print(sqrt(4225))
print()


# 5. დააგენერირეთ ნებისმიერი შემთხვევითი ათწილადი რიცხვი დიაპაზონიდან 0-დან 1-ის ჩათვლით. დაამრგვალეთ რიცხვი (3 ციფრი ათწილად ნაწილში) და დაბეჭდეთ.
print(example, "Example")
example += 1
print()
from random import uniform, randint
random_number = uniform(0, 1)
print("Random Number From 0 To 1", random_number, "Round In 3 Numbers After Dot", round(random_number, 3))
print()

# 6. დააგენერირეთ ნებისმიერი შემთხვევითი ათწილადი რიცხვი 100-დან 120-მდე. დაამრგვალეთ რიცხვი (1 ციფრი ათწილად ნაწილში) და ისე გამოიტანეთ.
print(example, "Example")
example += 1
print()
random_number = uniform(100, 120)
print(random_number)
print(round(random_number, 1))

#7. დააგენერირეთ 10 შემთხვევითი მთელი რიცხვი და დაბეჭდეთ ეკრანზე. მითითება: გამოიყენეთ ციკლის ოპერატორი.
print(example, "Example")
example += 1
print()
for i in range(1, 11):
    Number = randint(1, 12491247128947198246)
    print(Number)