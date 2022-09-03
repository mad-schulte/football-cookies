#!/usr/bin/env python


def add_to_dict(dictionary, letter, amountToIncrease=1):
    if letter == ' ':
        return

    letter = letter.lower()

    if letter in dictionary:
        dictionary[letter] += amountToIncrease
    else:
        dictionary[letter] = amountToIncrease


# histogram each ...?

# loop in reverse order; pick a letter that won't be required later and add ALL letters of that team to the required-later set
#

def find_letter_for_each_week():
    later_words = {}
    letters_results = []
    letter_with_team = {}

    for word in words.reverse():
        add_to_needed_later(later_words, word)
        result = find_nonrequired_letter(later_words, word)
        if (result != "NONE"):
            letters_results.add(result)
            letter_with_team[word] = result

    return letter_with_team


def add_to_needed_later(dictionary, word):
    for letter in word:
        letter = strip_and_lower(letter)

        if letter == "":
            continue
        
        if letter in dictionary:
            dictionary[letter] += 1 
        else:
            dictionary[letter] = 1
        

def find_nonrequired_letter(dictionary, word):
    for letter in word:
        if not letter_required_later(dictionary, letter):
            return letter

    return "NONE"
 

def letter_required_later(dictionary, letter):
    if letter == ' ':
        return

    if letter in dictionary:
        return True
    else:
        return False

def strip_and_lower(string):
    string = string.replace(" ","")
    string = string.lower()
    return string


if __name__ == '__main__':

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


    print()

