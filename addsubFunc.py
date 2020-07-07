#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
随机生成10以内加减法口算算式
'''
from random import randint,choice

def addsubFunc():
    c = 0
    while c < 100:
        a = randint(0,10)
        b = randint(0,10)
        s1 = s2 = 0
        s = choice([43,45])
        if s == 43:
            s1 = a + b
            if s1 <= 10:
                print('%d + %d = %d'%(a,b,s1))   
                c += 1
    
        else:
            s2 = a - b
            if s2 >= 0 and s2 <= 10:
                print('%d - %d = %d'%(a,b,s2))
                c += 1

if __name__ == '__main__':
    addsubFunc()
















