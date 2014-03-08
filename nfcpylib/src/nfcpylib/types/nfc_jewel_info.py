'''
Created on Feb 13, 2014

@author: chainer
'''

from ctypes import Structure, c_uint8
class NFC_JEWEL_INFO(Structure):
    _fields_ = [
                 ( 'btSensRes', c_uint8 * 2 ),
                 ( 'btId', c_uint8 * 4 )
                 ]