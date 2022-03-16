def between_markers(text: str, begin: str, end: str) -> str:
    if begin not in text and end not in text:
        return text
    elif begin not in text:
        return text.split(end)[0]
    elif end not in text:
        return text.split(begin)[1]
    else:
        text_after_begin_marker = text.split(begin)[1]
        if end not in text_after_begin_marker:
            return ''
        else:
            return text_after_begin_marker.split(end)[0]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')