'''
Created on Feb 13, 2014

@author: chainer
@note: c_long is ctypes equivalent to int in C  
'''

from ctypes import Structure, c_long

class NFC_MODULATION(Structure):
    _fields_ = [
                ( 'nmt', c_long ),#NFC_MODULATION_TYPE ),
                ( 'nbr', c_long ),#NFC_BAUD_RATE )
                ]