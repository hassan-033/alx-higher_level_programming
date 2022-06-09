#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numbers = [1, 5, 10, 50, 100, 500, 1000]
    roman_letter = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    if roman_string is None or type(roman_string) is not str:
        return 0
    integer = 0
    lenght = len(roman_string)
    for i, number in enumerate(roman_string):
        for x, letter in enumerate(roman_letter):
            if number == letter:
                if lenght == i + 1:
                    integer = integer + roman_numbers[x]
                    break
                elif letter == 'D':
                        if roman_string[i + 1] == roman_letter[x + 1]:
                            integer = integer - roman_numbers[x]
                            break
                        else:
                            integer = integer + roman_numbers[x]
                            break
                elif letter == "M":
                        integer = integer + roman_numbers[x]
                        break
                else:
                    if roman_string[i + 1] == roman_letter[x + 1]:
                        integer = integer - roman_numbers[x]
                        break
                    elif roman_string[i + 1] == roman_letter[x + 2]:
                        integer = integer - roman_numbers[x]
                        break
                    else:
                        integer = integer + roman_numbers[x]
                        break
    return integer
