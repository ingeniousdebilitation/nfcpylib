'''
Created on Feb 13, 2014

@author: chainer
'''

from ctypes import Structure, c_uint8
class NFC_ISO14443B2SR_INFO(Structure):
    _fields_ = [
                 ( 'abtUID', c_uint8 * 8 ),
                 ]