'''
Created on Feb 13, 2014

@author: chainer
@attention: There is problem with szUidLen. When it has c_size_t data type  like in nfc-types.h, then first abtUid byte is copied into szUidLen and other bytes are on abtUid
@
'''

from ctypes import Structure, c_uint8, c_size_t

class NFC_ISO14443A_INFO(Structure):  
    _fields_ = [
                ('d', c_uint8),
                 ( 'abtAtqa', c_uint8 ),
                 ( 'btSak', c_uint8 ),
                 ( 'szUidLen', c_uint8 * 4 ),   # c_size_t by melo byt, ale pak se prvni byte z abtUid umisti do szUidLen a v abtUid je druhy, treti, ctvrty a nuly
                 ( 'abtUid', c_uint8 * 10 ),
                 ( 'szAtsLen', c_size_t ),
                 ( 'abtAts', c_uint8 * 254 )    # Maximal theoretical ATS is FSD-2, FSD=256 for FSDI=8 in RATS
                 ]