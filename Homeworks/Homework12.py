# This Function will print which task is it
def next_task(x):
    print(x, "Task")

# Task 2

def task2(x, y, n):
    biggest = x
    leg1 = y
    leg2 = n
    if y > x:
        biggest = y
        leg1 = x
        leg2 = n
    if n > y:
        biggest = n
        leg1 = x
        leg2 = y
    if leg1 + leg2 > biggest:
        return True
    else:
        return False

# Task 3

def Task3():
    text = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
    temp_text = ""

    for i in range(len(text)):
        if "ლ" in text[i]:
            temp_text += "ნ"
        else:
            temp_text += text[i]
    print(temp_text)

next_task(2)

n1 = float(input("> "))
n2 = float(input("> "))
n3 = float(input("> "))

print(task2(n1, n2, n3))

next_task(3)

Task3()