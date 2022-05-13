file_obj = open('text.txt', 'r')
# file_obj2 = open('test2.txt', "r")
# file_obj3 = open('text3.txt', "w")

i = file_obj.read()
# n = file_ojbect2.read()
# file_ojbect3.write(n + i)
print(i.upper())


file_obj.close()
# file_obj2.close()
# file_obj3.close()