def checkio(text):
    letter_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter.isalpha():
            letter_dict[letter] = lower_text.count(letter)
    result = sorted(list(letter_dict.items()), key=lambda k_v: (-k_v[1], k_v[0]))
    return result[0][0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")