'''
Created on Feb 12, 2014

@author: chainer

@summary: Python ctypes-based wrapper for nfc_internal structure.
@see: http://www.libnfc.org/api/nfc-internal_8h_source.html

'''

from ctypes import Structure, c_bool, c_char
from src.nfcpylib.types.constants import DEVICE_NAME_LENGTH, NFC_BUFSIZE_CONNSTRING

class NFC_USER_DEFINED_DEVICE(Structure):
    
    _fields_ = [
                ( 'name', c_char * DEVICE_NAME_LENGTH ),        # char name[DEVICE_NAME_LENGTH];
                ( 'connstring', c_char * NFC_BUFSIZE_CONNSTRING),   # nfc_connstring connstring; typedef char nfc_connstring[NFC_BUFSIZE_CONNSTRING];
                ( 'optional', c_bool )                          # bool optional;
                ]


