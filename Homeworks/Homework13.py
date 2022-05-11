
# Next task printer function
def next_task(x):
    print(x, "Task")


# Task 1
def upper_symbol(x):
    print(x.upper())

# Task 2
def Task2(x, y, z):
    print("Ver gavige")

# Task 3
def contains_s():
    count = 0
    temp_text = ''
    text = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
    for i in range(20):
        if 'ს' == text[i]:
            count += 1
        temp_text += text[i]
    print(temp_text)
    print(f'"ს" Is For {count} Times')

# Task 4
def type_change(text):
    temp_number = ""
    for i in range(len(text)):
        if text[i].upper() is True:
            temp_number += text[i].lower()
        else:
            temp_number += text[i].upper()
    print(temp_number)



text_v = input("> ")
type_change(text_v)