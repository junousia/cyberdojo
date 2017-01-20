#!/usr/bin/env python2

def is_consistent(numbers):
    '''
    >>> is_consistent(['1234','1222','123'])
    False
    >>> is_consistent(['123','1234','321'])
    False
    >>> is_consistent(['123','1134','321'])
    True
    >>> is_consistent(['123','11234','321'])
    True
    '''
    root = dict()
    for number in numbers:
        current_dict = root
        for letter in number:
            current_dict = current_dict.setdefault(letter, {})
            if 'end' in current_dict.keys():
                return False
        if current_dict:
            return False
        current_dict['end'] = True
    return True
