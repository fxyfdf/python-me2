#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from do_yield import each_ascii,yield_from


def main():
    for x in each_ascii('abc'):
        print(x) # => 'a', 'b', 'c'
    it = each_ascii('xyz')
    try:
        while True:
            print(next(it)) # => 'x', 'y', 'z'
    except StopIteration as s:
        print(s.value) # => '3 chars'

    # using yield from in main() will change main() from function to generator:
    # r = yield from each_ascii('hello')

    for ch in yield_from('hello'):
        pass
print (main)
#main()

if __name__ == '__main__':
    main()


