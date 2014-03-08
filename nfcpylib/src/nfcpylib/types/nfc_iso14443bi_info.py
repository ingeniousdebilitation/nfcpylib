'''
Created on Feb 13, 2014

@author: chainer
'''

from ctypes import Structure, c_uint8, c_size_t
class NFC_ISO14443BI_INFO(Structure):
    _fields_ = [
                 ( 'abtDIV', c_uint8 * 4 ),
                 ( 'btVerLog', c_uint8 ),
                 ( 'btConfig', c_uint8 ),
                 ( 'szAtrLen', c_size_t ),
                 ( 'abtAtr', c_uint8 * 33)
                 ]