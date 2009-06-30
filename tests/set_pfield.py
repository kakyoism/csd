#!/usr/bin/env python
'''Tests for set_pfield()'''

import sys
sys.path.append('../')
import score as s

def test(n, line, pf, v, expect):
    result = s.set_pfield(line, pf, v)
    did_pass = result == expect

    return did_pass, n, 'set_pfield()', str(expect), str(result)

print test(0, ' ', 0, '', ' ')
print test(1, '/* */', 0, '', '/* */')
print test(2, '/* */', 0, '', '/* */')
print test(3, '/* */ ', 0, '', '/* */ ')
print test(4, '/* */ /* */ ', 0, '', '/* */ /* */ ')
print test(5, 'i', 0, 'i', 'i')
print test(6, 'i', 0, 'f', 'f')
print test(7, '/* */ /* */ i', 0, 'f', '/* */ /* */ f')
print test(8, 'i 1', 1, '3', 'i 3')
print test(9, 'i 1 0 4 0.777', 4, '0.666', 'i 1 0 4 0.666')
print test(10, 'i 1 0 $foo', 3, '$bar', 'i 1 0 $bar')
print test(11, 'i 1 0 [~ * 100 + 100]', 3, '[~ * 440 + 440]',
               'i 1 0 [~ * 440 + 440]')
print test(12, 'i 1 0 "foo"', 3, '"bar"', 'i 1 0 "bar"')
print test(13, 'i 1 0 "foo"', 3, '"bar"', 'i 1 0 "bar"')
print test(14, 'i 1 0 4', 4, 'asdf', 'i 1 0 4')
print test(15, 'i 1 0 4', -1, 'asdf', 'i 1 0 4')
print test(16, 'i 1 0 {{foo}}', 3, '{{bar}}', 'i 1 0 {{bar}}')
print test(17, 'i 1 0 4 ; my comment', 3, '4.1', 'i 1 0 4.1 ; my comment')
print test(18, 'i 1 0 4; my comment', 3, '4.1', 'i 1 0 4.1; my comment')
print test(19, 'i 1 0 .', 3, '4', 'i 1 0 4')
print test(20, 'i 1 0 <', 3, '.', 'i 1 0 .')
print test(21, 'i 1 0 (', 3, '.', 'i 1 0 .')
print test(22, 'i 1 0 )', 3, '.', 'i 1 0 .')
print test(23, 'i 1 0 ~', 3, '.', 'i 1 0 .')
print test(24, 'i 1 0 +', 3, '.', 'i 1 0 .')
print test(25, 'i 1 0 ^+1', 3, '.', 'i 1 0 .')
print test(26, 'i 1 0 ^-1', 3, '.', 'i 1 0 .')
print test(27, 'i 1 0 !', 3, '.', 'i 1 0 .')
print test(28, 'i 1 0 np4', 3, 'np5', 'i 1 0 np5')
print test(29, 'i 1 0 pp4', 3, 'np5', 'i 1 0 np5')
print test(30, 'i 1 0 np14', 3, 'np5', 'i 1 0 np5')
print test(21, 'i 1 0 pp14', 3, 'np5', 'i 1 0 np5')


