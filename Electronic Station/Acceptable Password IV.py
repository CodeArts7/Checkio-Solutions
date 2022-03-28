def is_acceptable_password(password: str) -> bool:
    numbers = 0
    for symbol in password:
        if symbol.isdigit():
            numbers += 1

    if len(password) in range(7, 10) and any(symbol.isdigit for symbol in password) and numbers < 6:
        return True
    elif len(password) > 9:
        return True
    return False


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")