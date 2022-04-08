nickname = str(input("Input Your Nickname: "))
print("Hallo,", nickname)

# Program starts here
weight = int(input("Input Your Weight: "))
weight_type = str(input("Input Which Type Inputted, (L)BS OR (K)G: "))

# Code
if weight_type == "L" or weight_type == "l":
    kg = weight / 2.2
    print("You Are", kg, "In Kg")
elif weight_type == "K" or weight_type == "k":
    lbs = weight * 2.2
    print("You Are", lbs, "In Lbs")