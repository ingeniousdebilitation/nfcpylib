'''
Created on Feb 13, 2014

@author: chainer
'''

from ctypes import Structure, c_uint8, c_size_t, c_long

class NFC_DEP_INFO(Structure):
    _fields_ = [
                 ( 'abtNFCID3', c_uint8 * 10 ),
                 ( 'btDID', c_uint8 ),
                 ( 'btBS', c_uint8 ),
                 ( 'btBR', c_uint8 ),
                 ( 'btTO', c_uint8 ),
                 ( 'btPP', c_uint8 ),
                 ( 'abtGB', c_uint8 * 8),
                 ( 'szGB', c_size_t ),
                 ( 'ndm', c_long )#NFC_DEP_MODE )
                 ]