def text_stat(input_text):

    input_text_str = '\n'.join(input_text).lower()

    print('Был использован следующий текст:')
    print('<--- Текст ---')
    for i in input_text:
        print(i)
    print('--- Текст --->')

    def stat_count(text):
        key_ = {i for i in text }
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

main_dict = dict(text_stat(main_input()))

print ('Всего цифр в тексте = {}'.format(main_dict.get('digits')))
print ('Всего строк в тексте = {}'.format(main_dict.get('lines')))
print_dict(main_dict.get('chars_stat'), 'символов')
print_dict(main_dict.get('words_stat'), 'слов')