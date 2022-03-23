def translation(text: str) -> str:
    text = input('Введите текст: ')
    vocabulary = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                               'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                               "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                               'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
    try:
        return text.translate(vocabulary)
    except TypeError:
        return 'К сожалению произошла ошибка...' \
               '\nМы не можем транслировать данный текст.' \
               '\nОбратитесь в службу поддержки по ссылке ниже.'


print(translation(''))