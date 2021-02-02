
def get_key():
    key = 0
    max_len_key = 1114111
    while key == 0:
        try:
            key = int(input('ключ: '))
            if key > max_len_key or key < 1:
                key = 0
                print("Ключ должен быть в промежутке 1 < X < {}".format(max_len_key, max_len_key))
            else:
                return key
        except ValueError:
            print('Ключ должен быть целым числом')


def code(message, key):
    crypt = ''
    for i in message:
        crypt += chr(ord(i) ^ key)
    return crypt


if __name__ == "__main__":
    z = int(input('1.файл \n2.рукописный ввод \n'))
    if z == 1:
        file_name = input('разместите файл в дирректории программы и введите его имя: ')
        with open('{}.txt'.format(file_name), 'rt', encoding="utf-8") as f:
            key = get_key()
            res = code(f.read(), key)
            with open('{}'.format(file_name + '_crypt.txt'), 'w', encoding="utf-8") as w:
                w.write(res)

    if z == 2:
        inp = input('слово: ')
        key = get_key()
        res = code(inp, key)
        print('Результат:', res)
