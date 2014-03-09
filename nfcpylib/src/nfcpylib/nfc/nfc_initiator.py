'''
Created on Mar 8, 2014

@author: ingenious debilitation
'''
from ctypes import CDLL
from src.nfcpylib.nfc.nfc_error import NfcError

class NfcInitiator(object):
    '''
    classdocs
    '''
    
    LIBPATH = "/usr/lib/libnfc.so"

   
    def __init__(self, device, secure=False, libpath=LIBPATH):
        '''
        Initialize NFC device as initiator (reader), or as initiator with its secure element
        
        Args:
            device (NfcDevice): NfcDevice instance.
            secure (bool, optional): Secure initialization when True. Defaults to False.
            libpath (string, optional): LibNfc library path. Defaults to LIBPATH constant.
        
        Returns:
            None
            
        Raises:
            NfcError: When LibNfc do not returns NFC_SUCCESS
        '''
        
        self.lib = CDLL(libpath)
        
        if not secure:
            self.initCommon(device)
        else:
            self.initSecureElement(device)
       
    
    def __initCommon__(self, device):
        status = self.lib.nfc_initiator_init(device.device)
        
        if status != NfcError.NFC_SUCCESS:
            raise NfcError(status)
        
    def __initSecureElement__(self, device):
        raise NotImplementedError
    
        
        