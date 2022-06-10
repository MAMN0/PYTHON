dict = {
    "key1": "bike",
    "key2": "car",
    "key3": "bus"
}
dict.pop("key1") # შლის ლექსიკონიდან გადაცემულ გასაღების მნიშვნელობას ლექსიკონიდან.
print(dict)

dict = {
    "key1": "bike",
    "key2": "car",
    "key3": "bus"
}
x = dict.keys() # გვიბრუნებს ყველა გასაღებს
print(x)

dict["key4"] = "airplane" # ეს არის ჩანაწერი თუ როგორ დავამატოთ ახალი გასაღები და მისი მნიშვნელობა
print(dict)