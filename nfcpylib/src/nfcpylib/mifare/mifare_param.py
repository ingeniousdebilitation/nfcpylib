'''
Created on Feb 14, 2014

@author: chainer
'''

from ctypes import Union
from src.nfcpylib.mifare.mifare_param_auth import MIFARE_PARAM_AUTH
from src.nfcpylib.mifare.mifare_param_data import MIFARE_PARAM_DATA
from src.nfcpylib.mifare.mifare_param_value import MIFARE_PARAM_VALUE

class MIFARE_PARAM(Union):  
    _fields_ = [
                ( 'mpa', MIFARE_PARAM_AUTH ),
                ( 'mpd', MIFARE_PARAM_DATA ),
                ( 'mpv', MIFARE_PARAM_VALUE)
                 ]