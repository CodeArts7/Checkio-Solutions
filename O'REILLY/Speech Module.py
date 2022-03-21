FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    result = []
    if not 0 <= number < 1000:
        return "Outisde the loop"
    if number == 0:
        result.append('zero')
    elif 0 < number <= 9:
        result.append(FIRST_TEN[number - 1])
    elif 10 <= number <= 19:
        result.append(SECOND_TEN[number - 10])
    elif 20 <= number <= 99:
        if number % 10 == 0:
            result.append(OTHER_TENS[number // 10 - 2])
        else:
            result.append(OTHER_TENS[number // 10 - 2] + " " + FIRST_TEN[number % 10 - 1])
    elif 100 <= number < 1000:
        if number % 100 == 0:
            result.append(FIRST_TEN[(number // 100) - 1] + " " + HUNDRED)
        else:
            result.append(FIRST_TEN[(number // 100) - 1] + " " + HUNDRED + " " + checkio(number % 100))

    return ' '.join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')