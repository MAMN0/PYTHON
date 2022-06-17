def morse_to_text(text):
    with open("morsescode.txt", "r") as morse:
        morse_dict = {}
        for i in morse:
            morse_dict[i[2:-1]] = i[0]
    managed_text_list = text.split()
    result = ""
    for i in managed_text_list:
        if i in morse_dict.keys():
            result += f'{morse_dict[i]}'
            continue
        if i == "|":
            result += " "
            continue
    return result

def text_to_morse(text):
    morse_dict = {' ': '|'}
    with open("morsescode.txt", "r") as morse:
        for i in morse:
            let, mor = i.split('\t')
            morse_dict[let] = mor[:-1]

    result = ''
    for i in text.upper():
        result += f'{morse_dict[i]} '

    return result
def decrypt():
    decrypt_answer = input("Input Your Morse Text: ")
    print(morse_to_text(decrypt_answer))

def translate():
    translate_answer = input("Input Your Text: ")
    print(text_to_morse(translate_answer))


while True:
    answer = input("Which do you want to Decrypt or Translate? (D/T) >")
    if answer.upper() == "D":
        decrypt()
    elif answer.upper() == "T":
        translate()