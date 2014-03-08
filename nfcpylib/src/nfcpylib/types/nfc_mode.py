'''
Created on Feb 13, 2014

@author: chainer
'''
from ctypes import c_long

class NFC_MODE(object): # enum hack in Python 2.7
    N_TARGET = c_long(1)
    N_INITIATOR = c_long(2)
