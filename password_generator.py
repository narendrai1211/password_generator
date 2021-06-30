import random

DIGITS = [str(i) for i in range(0, 10)]

LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<', '^', '&', '-', '+', '\\', '`', '"', '\'', '!']

combined_list = LOWERCASE + DIGITS + UPCASE_CHARACTERS + SYMBOLS


def pass_gen(num_chars):
    password_ = ''
    for i in range(0, int(num_chars)):
        password_ = password_ + random.choice(combined_list)
    return password_
