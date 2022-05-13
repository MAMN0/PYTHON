#1. დაწერეთ პროგრამა, რომლის მეშვეობით შექმნით ფაილს იმავე დირექტორიაში (საქაღალდეში), ჩაწერეთ მასში ნებისმიერი ტექსტი და დახურეთ ფაილი.
file_object = open('homeworkfile.txt', 'w')
print(file_object.write("asdfjakfh"))
file_object.close()
# 2. დაწერეთ პროგრამა, რომლის მეშვეობით გახსნით ფაილს, წაიკითხავთ კონტენტს და დაბეჭდავთ ეკრანზე. დაითვალეთ სიმბოლოების რაოდენობა ფაილში.
file_object = open('homeworkfile.txt', 'r')
print(len(file_object.read()))
file_object.close()
# #3. დაწერეთ პროგრამა, რომლის მეშვეობით გახსნით უკვე არსებულ ფაილს და ბოლოში დაამატეთ თქვენთვის სასურველი ტექსტი.
file_object = open('homeworkfile.txt', 'a')
file_object.write('\nhello world')
file_object.close()
#4. დაწერეთ პროგრამა რომელიც წაიკითხავს ინფორმაციას ერთი ფაილიდან და ჩააკოპირებს მეორე (ახალ) ფაილში.
file_object = open('homeworkfile.txt', 'r')
copytext = file_object.read()
file_object2 = open('testfile.txt', 'a')
file_object2.write(copytext)
file_object.close()
file_object2.close()