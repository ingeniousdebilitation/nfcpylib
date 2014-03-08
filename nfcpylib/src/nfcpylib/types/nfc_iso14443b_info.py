'''
Created on Feb 13, 2014

@author: chainer
'''

from ctypes import Structure, c_uint8
class NFC_ISO14443B_INFO(Structure):
    _fields_ = [
                 ( 'abtPupi', c_uint8 * 4 ),
                 ( 'abtApplicationData', c_uint8 * 4 ),
                 ( 'abtProtocolInfo', c_uint8 *3 ),
                 ( 'ui8CardIdentifier', c_uint8 ),
                 ]