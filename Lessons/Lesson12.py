def count(a, text):
    count = 0
    for i in range(len(text)):
        if a in text[i]:
            count += 1
    return count

symbol = ""
symbol_count = 0


text = input("> ")

for i in range(len(text)):
    if count(text[i], text) > symbol_count:
        symbol = text[i]
        symbol_count = count(text[i], text)
print(symbol)
print(symbol_count)