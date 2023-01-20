from itertools import filterfalse
from math import *
from pickle import FALSE
from random import choice
from re import *
import string

def salasona (k:int)->str:
    sala=""
    for i in range (k):
        t=choice(string.ascii_letters)
        num=choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        sala+=choice(t_num)
    return sala

def isesalasona (sona):
    s=list(sona)
    tupper=False
    tdigit=False
    for i in s:
        if i.isupper():
            tupper=True
        if i.isdigit():
            tdigit=True
    if tupper==True and tdigit==True and len(s)>5:
        print("Great! Your pass is :", sona)
    else:
        print("Your pass is too weak, write one upper letter and number")