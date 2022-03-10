def non_empty_lines(text: str) -> int:
    lines = text.splitlines()
    while '' in lines:
        lines.remove('')
    count = 0
    for i in lines:
        if i.isspace():
            count += 1
    return len(lines) - count

if __name__ == '__main__':
    print("Example:")
    print(non_empty_lines('one simple line\n'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert non_empty_lines('one simple line\n') == 1
    assert non_empty_lines('') == 0
    assert non_empty_lines('\nonly one line\n            ') == 1
    assert non_empty_lines('''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            ''') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")