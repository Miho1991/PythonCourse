
def text_stat(input_text, *args):

    input_text_str = '\n'.join(input_text).lower()

    print('Был использован следующий текст:')
    print('<--- Текст ---')
    for i in input_text:
        print(i)
    print('--- Текст --->')
    print()

    inp_arg = []
    for i in args:
        if type(i) == list:
            inp_arg.extend(i)
        elif type(i)== str:
            inp_arg.append(i)
        elif type(i) == dict:
            for n in dict.values():
                inp_arg.append(n)
        else:
            for n in i:
                inp_arg.append(n)

    inp_list_text = [i for i in input_text_str.split()]

    for i in input_text_str.split():
        for j in inp_arg:
            if i==j.lower():
                inp_list_text.remove(i)

    input_text_str = ''
    input_text_str = ' '.join(inp_list_text)

    def stat_count(text):
        key_ = {i for i in text}
        return {i: text.count(i) for i in key_}

    def digit_count(text):
        digits_ = [i for i in text if i.isdigit()]
        return len(digits_)

    digits = digit_count(input_text_str)
    chars_stat = stat_count(input_text_str)
    words_stat = stat_count(input_text_str.split())

    main_dict_def = {'digits': digits, 'lines':len(input_text), 'chars_stat':chars_stat, 'words_stat':words_stat}
    return main_dict_def

def print_dict(dict_: dict, word):
    print(' <--- Статистика {} --- '.format(word))
    for k, v in sorted(dict_.items()):
        print('{} = {}'.format(repr(k), v))
    print(' --- Статистика {} ---> '.format(word))
    print()

def main_input():
    list_in = []
    print('Введите текст >>> ')

    while True:
        text = input()
        if text=="":
            return list_in
        else:
            list_in.append(text)

text_inp = main_input()

main_dict = dict(text_stat(text_inp))

print ('Всего цифр в тексте = {}'.format(main_dict.get('digits')))
print ('Всего строк в тексте = {}'.format(main_dict.get('lines')))
print_dict(main_dict.get('chars_stat'), 'символов')
print_dict(main_dict.get('words_stat'), 'слов')
