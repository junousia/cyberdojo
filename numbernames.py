#!/usr/bin/env python2

from sys import argv
from collections import OrderedDict

'''
Spell out a number. For example

      99 --> ninety nine
     300 --> three hundred
     310 --> three hundred and ten
    1501 --> one thousand, five hundred and one
   12609 --> twelve thousand, six hundred and nine
  512607 --> five hundred and twelve thousand,
             six hundred and seven
43112603 --> forty three million, one hundred and
             twelve thousand,
             six hundred and three

[Source http://rosettacode.org]
'''

extended_num = {0: 'zero',
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten',
                11: 'eleven',
                12: 'twelve',
                13: 'thirteen',
                14: 'fourteen',
                15: 'fifteen',
                16: 'sixteen',
                17: 'seventeen',
                18: 'eighteen',
                19: 'nineteen'}

extended_tens = {2: 'twenty',
                 3: 'thirty',
                 4: 'forty',
                 5: 'fifty',
                 6: 'sixty',
                 7: 'seventy',
                 8: 'eighty',
                 9: 'ninety'}

extended_huge_numbers = OrderedDict([(10 ** 24, "septillion"),
                                     (10 ** 21, "sextillion"),
                                     (10 ** 18, "quintillion"),
                                     (10 ** 15, "quadrillion"),
                                     (10 ** 12, "trillion"),
                                     (10 ** 9, "billion"),
                                     (10 ** 6, "million"),
                                     (10 ** 3, "thousand"),
                                     (10 ** 2, "hundred")])


def extend(number):
    '''
    >>> extend(1000)
    'one thousand'
    >>> extend(1001)
    'one thousand and one'
    >>> extend(1111111)
    'one million, one hundred and eleven thousand, one hundred and eleven'
    >>> extend(43112603)
    'forty three million, one hundred and twelve thousand, six hundred and three'

    >>> extend(99)
    'ninety nine'
    >>> extend(300)
    'three hundred'
    >>> extend(310)
    'three hundred and ten'
    >>> extend(1501)
    'one thousand, five hundred and one'
    >>> extend(12609)
    'twelve thousand, six hundred and nine'
    >>> extend(512607)
    'five hundred and twelve thousand, six hundred and seven'
    >>> extend(1111111111111111)
    'one quadrillion, one hundred and eleven trillion, one hundred and eleven billion, one hundred and eleven million, one hundred and eleven thousand, one hundred and eleven'
    '''

    answer = ''

    for key, value in extended_huge_numbers.iteritems():
        count, remainder = divmod(number, key)
        if count:
            answer += ', ' if answer else ''
            answer += '%s %s' % (extend(count), value)
            number = remainder

    tens, singles = divmod(remainder, 10)
    answer += ' and ' if answer and (singles or tens) else ''

    if tens > 1:
        answer += '%s' % extended_tens[tens]
        answer += ' ' if singles else ''
    if tens == 1:
        singles += tens * 10
        answer += '%s' % extended_num[singles]
    elif singles:
        answer += '%s' % extended_num[singles]

    return answer

if __name__ == "__main__":
    print extend(int(argv[1]))
