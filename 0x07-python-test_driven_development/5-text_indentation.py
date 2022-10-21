#!/usr/bin/python3

def text_indentation(text):
    _str = '.:?'
    if type(text) is not str:
        raise TypeError('text must be a string')
    for c in _str:
        text = str(c + '\n\n').join(s.strip() for s in text.split(c))
        print(text, end='')
        if len(text) > 0 and text[-1] in _str:
            print('\n')

