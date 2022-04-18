def saving(original_text):
    textfile = open('output.md', 'w')
    textfile.write(original_text)
    textfile.close()


def list_constructor(original_text, type_of_list):
    if type_of_list == 'ordered-list':
        while True:
            rows = int(input('Number of rows: '))
            if rows > 0:
                break
            else:
                print('The number of rows should be greater than zero')
                continue
        for i in range(rows):
            each_one = input(f'Row #{i + 1}: ')
            original_text += f'{i + 1}. ' + each_one + '\n'
        return original_text
    elif type_of_list == 'unordered-list':
        while True:
            rows = int(input('Number of rows: '))
            if rows > 0:
                break
            else:
                print('The number of rows should be greater than zero')
                continue
        for i in range(rows):
            each_one = input(f'Row #{i + 1}: ')
            original_text += f'* ' + each_one + '\n'
        return original_text
    
    
def plain_text(original_text):
    new_text = input('Text: ')
    return original_text + new_text


def bold(original_text):
    new_text = input('Text: ')
    new_text = '**' + new_text + '**'
    return original_text + new_text


def italic(original_text):
    new_text = input('Text: ')
    new_text = '*' + new_text + '*'
    return original_text + new_text


def inline_code(original_text):
    new_text = input('Text: ')
    new_text = '`' + new_text + '`'
    return original_text + new_text


def link(original_text):
    label = input('Label: ')
    url = input('URL: ')
    return original_text + '[' + label + '](' + url + ')'


def header(original_text):
    while True:
        level = int(input('Level: '))
        if 1 <= level <= 6:
            break
        else:
            print('The level should be within the range of 1 to 6')
            continue
    new_text = input('Text: ')
    return original_text + '#' * level + ' ' + new_text + '\n'


def new_line(original_text):
    return original_text + '\n'


text_itself = ''
formatters = 'plain bold italic header link inline-code new-line ordered-list unordered-list'
formatter = ''
while True:
    formatter = input('Choose a formatter: ')
    if formatter in formatters:
        if formatter == 'plain':
            text_itself = plain_text(text_itself)
            print(text_itself)
        elif formatter == 'bold':
            text_itself = bold(text_itself)
            print(text_itself)
        elif formatter == 'italic':
            text_itself = italic(text_itself)
            print(text_itself)
        elif formatter == 'inline-code':
            text_itself = inline_code(text_itself)
            print(text_itself)
        elif formatter == 'link':
            text_itself = link(text_itself)
            print(text_itself)
        elif formatter == 'header':
            text_itself = header(text_itself)
            print(text_itself)
        elif formatter == 'new-line':
            text_itself = new_line(text_itself)
            print(text_itself)
        elif formatter == 'ordered-list' or formatter == 'unordered-list':
            text_itself = list_constructor(text_itself, formatter)
            print(text_itself)
        continue
    elif formatter == '!help':
        print(f'Available formatters: {formatters}\nSpecial commands: !help !done')
    elif formatter == '!done':
        saving(text_itself)
        break
    else:
        print('Unknown formatting type or command')
