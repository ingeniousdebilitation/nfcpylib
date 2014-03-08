'''
Created on Feb 13, 2014

@author: chainer
'''

from ctypes import Structure, c_uint8
class NFC_ISO14443b2CT_INFO(Structure):
    _fields_ = [
                ( 'abtUID', c_uint8 * 4),
                ( 'btProdCode', c_uint8 ),
                ( 'btFabCode', c_uint8 ),
                ]