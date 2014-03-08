'''
Created on Feb 13, 2014

@author: chainer
'''

from ctypes import Structure, c_uint8, c_size_t
class NFC_FELICA_INFO(Structure):
    _fields_ = [
                 ( 'szLen', c_size_t),
                 ( 'btResCode', c_uint8),
                 ( 'abtId', c_uint8 * 8),
                 ( 'abtPad', c_uint8 * 8),
                 ( 'abtSysCode', c_uint8 * 2),
                 ]