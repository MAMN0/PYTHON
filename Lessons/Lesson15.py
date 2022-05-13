file_ojbect = open('text.txt', 'r')
file_ojbect2 = open('test2.txt', "r")
file_ojbect3 = open('text3.txt', "w")

i = file_ojbect.read()
n = file_ojbect2.read()
file_ojbect3.write(n + i)

file_ojbect3.close()
file_ojbect2.close()
file_ojbect.close()