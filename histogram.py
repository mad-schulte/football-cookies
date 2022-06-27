#!/usr/bin/env python

def add_to_dict(dictionary, letter, amountToIncrease=1):
    if letter == ' ':
        return

    letter = letter.lower()

    if letter in dictionary:
        dictionary[letter] += amountToIncrease
    else:
        dictionary[letter] = amountToIncrease

test_string = "Buckeyes \n Thundering Herd \n Golden Bears \n Tarheels \n Cougars \n Cardinal \n Rebels \n Orange \n Tigers \n Midshipmen \n Eagles \n Trojans"

req_letters = dict()

for line in test_string.splitlines():
    #print(line.strip())
    line_hist = dict()
    for letter in line:
        add_to_dict(line_hist, letter)
    #print(line_hist)

    for key in line_hist:
        if (key in req_letters) and (line_hist[key] > req_letters[key]):
            add_to_dict(req_letters, key, line_hist[key] - req_letters[key])
        elif key not in req_letters:
            add_to_dict(req_letters, key, line_hist[key])


sorted_letters = sorted(req_letters.keys())
for letter in sorted_letters:
    print(letter + ": " + str(req_letters[letter]))
