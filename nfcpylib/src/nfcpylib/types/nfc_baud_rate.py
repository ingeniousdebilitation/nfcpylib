'''
Created on Feb 13, 2014

@author: chainer
'''
from ctypes import c_long

class NFC_BAUD_RATE(object): # enum hack in Python 2.7
    NBR_UNDEFINED = c_long(0)
    NBR_106 = c_long(1)
    NBR_212 = c_long(2)
    NBR_424 = c_long(3)
    NBR_847 = c_long(4)