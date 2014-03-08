'''
Created on Feb 13, 2014

@author: chainer
'''
from ctypes import Union
from wrapper.nfclib.types.nfc_iso14443a_info import NFC_ISO14443A_INFO
from wrapper.nfclib.types.nfc_felica_info import NFC_FELICA_INFO
from wrapper.nfclib.types.nfc_iso14443b_info import NFC_ISO14443B_INFO
from wrapper.nfclib.types.nfc_iso14443bi_info import NFC_ISO14443BI_INFO
from wrapper.nfclib.types.nfc_iso14443b2sr_info import NFC_ISO14443B2SR_INFO
from wrapper.nfclib.types.nfc_iso14443b2ct_info import NFC_ISO14443b2CT_INFO
from wrapper.nfclib.types.nfc_jewel_info import NFC_JEWEL_INFO
from wrapper.nfclib.types.nfc_dep_info import NFC_DEP_INFO

class NFC_TARGET_INFO(Union):
    _fields_ = [
        ( 'nai', NFC_ISO14443A_INFO ),
        ( 'nfi', NFC_FELICA_INFO ),
        ( 'nbi', NFC_ISO14443B_INFO ),
        ( 'nii', NFC_ISO14443BI_INFO ),
        ( 'nsi', NFC_ISO14443B2SR_INFO  ),
        ( 'nci', NFC_ISO14443b2CT_INFO ),
        ( 'nji', NFC_JEWEL_INFO ),
        ( 'ndi', NFC_DEP_INFO )
    ]
        