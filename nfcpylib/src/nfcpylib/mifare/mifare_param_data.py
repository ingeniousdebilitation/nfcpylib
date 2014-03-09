'''
Created on Feb 14, 2014

@author: chainer
'''

from ctypes import Structure, c_uint8
class MIFARE_PARAM_DATA(Structure):  
    _fields_ = [
                ('abtData', c_uint8 * 16 ),
                 ]