'''
Created on Feb 13, 2014

@author: chainer
'''
from ctypes import c_long
class NFC_MODULATION_TYPE(object): # enum hack in Python 2.7
    NMT_ISO14443A = c_long(1)
    NMT_JEWEL = c_long(2)
    NMT_ISO14443B = c_long(3)
    NMT_ISO14443BI = c_long(4 )     # pre-ISO14443B aka ISO/IEC 14443 B' or Type B'
    NMT_ISO14443B2SR = c_long(5)    # ISO14443-2B ST SRx
    NMT_ISO14443B2CT = c_long(6 )   # ISO14443-2B ASK CTx
    NMT_FELICA = c_long(6)
    NMT_DEP = c_long(7)