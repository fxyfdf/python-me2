#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#返回字符创 长度
def each_ascii(s):
    for ch in s:
        yield ord(ch)
    return "%s chars ------ " % len(s)
def yeild_from(s):

    r = yield from each_ascii(s)
    print (r)

"""

"""


"""
def main():
    for i in each_ascii('abc'):
        pass
        print (i)
    it = each_ascii('xyz')
    try:
        while True:
            print (next(it))
    except StopIteration as s:
        print (s.value)
    for ch in yeild_from('hello'):
        pass
main()
"""