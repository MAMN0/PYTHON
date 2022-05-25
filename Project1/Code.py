import random
# Global Variable
Acess = False

# First Action
answer = ""
while True:
    answer = input("Input Register or Login > ")
    if answer.lower() == "register" or answer.lower() == "login":
        break




# Register
with open("Data.txt", "a") as Data:
    with open("Data.txt", "r") as Data1:
        if answer.lower() == "register":
            name = input("Input Your Name > ")
            last_name = input("Input Your Last Name > ")
            while True:
                Password = input("Input Your New Password (First Symbol Must Be Upper) > ")
                if Password[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    break
            Mail = f'{name}.{last_name}@gmail.com'

            Data.write(f'{Mail},{Password},0,\n')
            print(f'Your Mail Is {Mail} And Your Password is {Password}.')

# Login
with open("Data.txt", "r") as Data:
    if answer.lower() == "login":
        Mail = input("Input Your Mail > ")
        Password = input("Input Your Password > ")
        is_mail = False
        is_password = False
        if "@gmail.com" in Mail:
            is_mail = True
        else:
            print("Wrong Mail")
        if Password[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            is_password = True
        else:
            print("Wrong Password")
        if is_mail and is_password:
            for i in Data:
                n = i.find(",")
                b = i.find(",", n + 1)
                score = int(i[b + 1:i.find(",", b + 1)])
                name = i[:i.find(".")]
                if i[:n] == Mail and i[n + 1:b]:
                    Acess = True
        if Acess:
            print(f'{Acess} Acess')
        else:
            print(f'{Acess} Acess')
        if is_mail and is_password == False:
            print("Wrong Password")
        if is_mail == False and is_password:
            print("Wrong Mail")

# Game
with open("Data.txt", "r") as Data:
    data = Data.read()
while True:
    game = False
    if Acess:
        print(f'Your Score Is {score} Points')
        action = input('Do You Want To Play "Right Numbers"? (Game or quit) > ')
        if action.lower() == "quit":
            print(f"Ok, Bye {name}")
            break
        elif action.lower() == "game": # Here started Game Code
            game = True
        if game:
            is_hint = True
            secret = random.randint(1,10)
            if secret > 4:
                hint = "Secret Number > 4"
            else:
                hint = "secret Number < 5"
            print(secret)
            i = -1
            print("In This Game, You Need To Enter Right Number.")
            print("1) This Number is Greater Than 0 And Lower Than 11.")
            print("2) If You Enter Right Number Your New Score Will Be Greater Than Your old Score")
            print("3) You Have 3 Chance.")
            print("Enjoyy <3")
            while i + 1 <= 3:
                i += 1
                if is_hint:
                    number = (input("Enter Right Number (You Can Use 1 hint, just type hint): "))
                    if number.lower() == "hint":
                        i -= 1
                        print(hint)
                        is_hint = False
                else:
                    number = int(input("Enter Right Number: "))
                if str(number) in "12345678910":
                    if number == secret or number == str(secret):
                        score += 1
                        print(f"You Won, Your Score Is {score}")
                        data = data.replace(data[data.find(",", data.find(Password)) + 1: data.find(",", data.find(",",data.find(Password)) + 1)],str(score))
                        break
                    if i + 1 == 3 and (number != secret or number != str(secret)):
                        print(f"You Lose, Your Score Is {score}")
                        break
with open("Data.txt", "w") as Data:
    Data.write(data)
print(data)