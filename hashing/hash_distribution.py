"""
    Author: Simon Westphahl <westphahl@gmail.com>
    Description: Testing hash distribution for multiplication and modulo.
    License: Public Domain
"""

from math import sqrt, floor

text = "Loraem ipbsum dcolor sdit ameet cosetetur sadpscing eltr seed dgam nosumy eird temdfpor inidunt udft lbore edft dlore mgasdna aquyam eabrat stied dfiam volptua Atat veron eods eukt ascsam ennt jullsto duno dors ehfht eajt rbum Stimet citlla kabsd gbergren notre sklma tkitatta sanlicttus ermist Lopprem isrum dmuolor siast amppet"

word_list = text.split()

k = (sqrt(5) - 1) / 2

mu = [0 for i in range(0, 16)]
mo = [0 for i in range(0, 16)]

def get_key(word):
    i = len(word)
    key = 0
    for char in word:
        i -= 1
        key += ord(char) * 80 ** i
    return key

print "%15s %25s %10s %10s \n" % ("Wort", "Key", "Mult", "Mod")

for word in word_list:
    mult = floor(((get_key(word) * k) % 16))
    mu[int(mult)] += 1
    mod = get_key(word) % 16
    mo[int(mod)] +=1

    print "%15s %25i %10i %10i" % (word, get_key(word), mult, mod)

print "Multiplikation: %s" % mu
print "Modulo: %s" % mo
