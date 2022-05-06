def symbol_count(a, text):
    count = 0
    for i in range(len(text)):
        if a in text[i]:
            count += 1
    return count

def place_char(a, text):
    symbol_place = ""
    for i in range(len(text)):
        if text[i] == a:
            symbol_place += str(i) + " "
    return symbol_place
symbol = ""
symbol_count_v = 0


text = input("> ")

for i in range(len(text)):
    if symbol_count(text[i], text) > symbol_count_v:
        symbol = text[i]
        symbol_count_v = symbol_count(text[i], text)
print(symbol)
print(place_char(symbol, text))
print(symbol_count_v)
