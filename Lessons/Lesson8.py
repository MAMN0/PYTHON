number = int(input('input number: '))

temp_number = number
count = 0
num_sum = 0

while temp_number >= 1:
    num_sum = temp_number
    temp_number //= 10

print(num_sum)