asterisk_long = 1
for i in range(1, 10):
    if i == asterisk_long:
        print("*******")
        asterisk_long += 4
    else:
        print("*     *")

print()

i = 1
while i < 11:
    if i < 6:
        asterisk_long = i
    else:
        asterisk_long -= 1
    print("*" * asterisk_long)
    i += 1