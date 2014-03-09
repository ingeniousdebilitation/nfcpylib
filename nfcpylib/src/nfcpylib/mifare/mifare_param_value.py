'''
Created on Feb 14, 2014

@author: chainer
'''

from ctypes import Structure, c_uint8
class MIFARE_PARAM_VALUE(Structure):  
    _fields_ = [
                ('abtValue', c_uint8 * 4 ),
                 ]