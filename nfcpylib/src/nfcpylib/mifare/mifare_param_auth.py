'''
Created on Feb 14, 2014

@author: chainer
'''

from ctypes import Structure, c_uint8

class MIFARE_PARAM_AUTH(Structure):  
    _fields_ = [
                ('abtKey', c_uint8 * 6 ),
                ('abtAuthUid', c_uint8 * 4 )
                 ]