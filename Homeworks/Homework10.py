x = 0
def example():
    global x
    x += 1
    return x
print(example(), "Example")
print()
# 1. შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის (დააბრუნებს) მათ საშუალო არითმეტიკულს. გამოიძახეთ
# ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის და დაბეჭდეთ შედეგი.
def task1(x, y):
    return (x + y) / 2
number_x = float(input("Input Number: "))
number_y = float(input("Input NUmber: "))
print(task1(number_x, number_y))
print()
print(example(), "Example")
print()
#2. დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის მათ საშუალო არითმეტიკულს და დაბეჭდავს შედეგს (გაითვალისწინეთ რომ დაბეჭდვა უნდა მოხდეს ფუნქციის შიგნით - ფუნქცია
#  არ აბრუნებს მნიშვნელობას). გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის.
def task2(x, y):
    print((x + y) / 2)
number_x = float(input("Input Number: "))
number_y = float(input("Input NUmber: "))
task2(number_x, number_y)
number_x = float(input("Input Number: "))
number_y = float(input("Input NUmber: "))
task2(number_x, number_y)
number_x = float(input("Input Number: "))
number_y = float(input("Input NUmber: "))
task2(number_x, number_y)
print()
print(example(), "Example")
print()
# 3. შექმენით ფუნქცია, რომელიც დაითვლის (დააბრუნებს) არგუმენტად გადაცემული რიცხვის კუბს. გამოიძახეთ ფუნქცია რამდენიმეჯერ და დაბეჭდეთ მიღებული შედეგი.
number_x = float(input("Input Number: "))
def qbrt(x):
    return x * x * x
print(qbrt(number_x))

print()
print(example(), "example")
print()

# 4. შექმენით ფუნქცია, რომელიც დაითვლის (დააბრუნებს) ორ რიცხვს შორის მინიმალურ მნიშვნელობას. გამოიძახეთ ფუნქცია და დაბეჭდეთ შედეგი. (პარამეტრად გადაეცით ნებისმიერი ორი რიცხვი).
def min(x, y):
    if x < y:
        return x
    else:
        return y

number_x = float(input("Input Number: "))
number_y = float(input("Input Number: "))

print(min(number_x, number_y))

print()
print(example(), "Example")
print()

# 5. დაწერეთ ფუნქცია, რომელიც შეამოწმებს პარამეტრად გადაცემული რიცხვი არის თუ არა კენტი. თუ კენტია, დააბრუნოს მნიშვნელობა True,
# თუ არადა - False. შეამოწმეთ რამდენიმე რიცხვისთვის და დაბეჭდეთ შედეგი.

def is_not_even(x):
    if x % 2 == 1:
        return True
    else:
        return False
number_x = int(input("Input Number: "))
print(is_not_even(number_x))
number_x = int(input("Input Number: "))
print(is_not_even(number_x))

print()
print(example(), "Example")
print()

# 6. დაწერეთ ფუნქცია, რომელიც დაითვლის (დააბრუნებს) პარამეტრად გადაცემული რიცხვის ფაქტორიალს და დაბეჭდეთ შედეგი სხვადასხვა რიცხვებისთვის.
def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f
print(factorial(5))

print()

print(example(), "Example")
print()

# 7. დაწერეთ უპარამეტრო ფუნქცია რომელიც ეკრანზე ბეჭდავს შემდეგ ტექსტს: “Hello World”. (გაითვალისწინეთ რომ ფუნქცია არ აბრუნებს მნიშვნელობას).
def letter():
    print('Hello World')
letter()
print()

print(example(), "Example")
print()

# 8. დაწერეთ ფუნქცია, რომელიც დაადგენს არის თუ არა პარამეტრად გადაცემული რიცხვი მარტივი რიცხვი.
def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
            break
        else:
            return True
number_x = int(input("Input Number: "))
if prime(number_x):
    print(number_x, "Is Prime")
else:
    print(number_x, "Is Not Prime")