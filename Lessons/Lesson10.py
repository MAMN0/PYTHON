# Geometric Examples
asterisk_long = 1
for i in range(1, 10):
    if i == asterisk_long:
        print("* * * * * *")
        asterisk_long += 4
    else:
        print("*         *")

print()

i = 1
while i < 11:
    if i < 6:
        asterisk_long = i
    else:
        asterisk_long -= 1
    print("* " * asterisk_long)
    i += 1


# Functions
def something():
    print("Something")
something()


# Return Functions
def return_sum():
    i = 3 + 6
    return i

sum = return_sum()
print("Sum is:", sum)

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

age = int(input("> "))
print(is_even(age))
if is_even(age):
    print("luwia")
else:
    print("kentia")

print()

def add(x, y):
    """
    Hallo,
    This is Function, Where You Can Input 2 Numbers
    """
    return x + y

print(add(4, 6))

help(add)