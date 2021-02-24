first_word = input()
second_word = input()

def get_summ(one, two, delimeter = '&'):
    whole_word = one + " " + delimeter + " " + two
    return whole_word.upper()

print(get_summ(first_word, second_word))