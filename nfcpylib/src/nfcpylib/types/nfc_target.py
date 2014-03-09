'''
Created on Feb 13, 2014

@author: chainer
'''

from ctypes import Structure
from src.nfcpylib.types.nfc_target_info import NFC_TARGET_INFO
from src.nfcpylib.types.nfc_modulation import NFC_MODULATION

class NFC_TARGET(Structure):
    _fields_ = [
                ( 'nti', NFC_TARGET_INFO ),
                ( 'nm', NFC_MODULATION )
                ]