len_uni = 1114111


def get_key():
    key = 0
    while key == 0:
        try:
            key = int(input('ключ: '))
            if key > len_uni or key < -len_uni:
                key = 0
                print("Ключ должен быть в промежутке -{} < X < {}".format(len_uni, len_uni))
            else:
                return key
        except ValueError:
            print('Ключ должен быть числом')


def code(message, key):
    crypt = ''
    for i in message:
        if ord(i) + key > len_uni - 1:
            crypt += chr((ord(i) + key) - len_uni)
        elif ord(i) + key < 0:
            crypt += chr((ord(i) + key) + len_uni)
        else:
            crypt += chr(ord(i) + key)
    return crypt


if __name__ == "__main__":
    y = int(input('1.закодировать \n2.декодировать \n'))
    if y == 1:
        z = int(input('1.файл \n2.рукописный ввод \n'))
        if z == 1:
            file_name = input('разместите файл в дирректории программы и введите его имя: ')
            with open('{}.txt'.format(file_name), 'rt', encoding="utf-8") as f:
                key = get_key()
                res = code(f.read(), key)
                with open('{}'.format(file_name + '_encode.txt'), 'w', encoding="utf-8") as w:
                    w.write(res)

        if z == 2:
            inp = input('слово: ')
            key = get_key()
            res = code(inp, key)
            print('Результат:', res)
    if y == 2:
        z = int(input('1.файл \n2.рукописный ввод \n'))
        if z == 1:
            file_name = input('разместите файл в дирректории программы и введите его имя: ')
            with open('{}_encode.txt'.format(file_name), 'rt', encoding="utf-8") as f:
                key = -get_key()
                res = code(f.read(), key)
                with open('{}'.format(file_name + '_decode.txt'), 'w', encoding="utf-8") as w:
                    w.write(res)

        if z == 2:
            inp = input('слово: ')
            key = -get_key()
            res = code(inp, key)
            print('Результат:', res)