'''
Created on Feb 12, 2014

@author: ingenious debilitation
@summary: Python ctypes-based wrapper for nfc_device structure. 
@attention: Structure nfc_driver is not so clear, so it is incomplete for now. 
@see: http://www.libnfc.org/api/structnfc__device.html
@see: http://www.libnfc.org/api/nfc-internal_8h_source.html
@see: http://www.libnfc.org/api/group__dev.html
@todo: implement listDevices method
@todo: driver structure
@todo: connstrings structure

'''
from ctypes import Structure, c_bool, c_char, c_uint8, c_int, POINTER, CDLL
from src.nfcpylib.nfc.nfc_context import NFC_CONTEXT, NfcContext
from src.nfcpylib.types.constants import NFC_BUFSIZE_CONNSTRING
from src.nfcpylib.nfc.nfc_error import NfcError
import ctypes

class NFC_DEVICE(Structure):
    DEVICE_NAME_LENGTH = 256
    DEVICE_PORT_LENGTH = 64 
    
    _fields_ = [
                # Ovladace nejsou tak zrejme jako ostanit casti, TODO!!!
                #('driver', TODO! ),                     # const struct nfc_driver *driver;
                #('driver_data', TODO! ),                # void *driver_data;
                #('chip_data', TODO! ),                  # void *chip_data;
                ( 'context', POINTER( NFC_CONTEXT ) ),  # const nfc_context *context;
                ( 'name', c_char * DEVICE_NAME_LENGTH ),        
                ( 'connstring', c_char * NFC_BUFSIZE_CONNSTRING),  
                ( 'bCrc', c_bool ),
                ( 'bPar', c_bool ),
                ( 'bEasyFraming', c_bool ),
                ( 'bAutoIso14443_4', c_bool ),
                ( 'btSupportByte', c_uint8 ),
                ( 'last_error', c_int  )                    
                ]
    

class NfcDevice(object):
    '''
    classdocs
    '''
    
    LIBPATH = "/usr/lib/libnfc.so"
    
    @property
    def device(self):
        return self._device
    
    @device.setter
    def device(self, device):
        self._device = device
        
    def __init__(self, context, connstring=None, libpath=LIBPATH):
        '''
        Constructor
        '''
        try:
            # Open shared library
            self.lib = CDLL(libpath)
        except OSError as e:
            raise e
        else:
            # Open device using context 
            self.lib.nfc_open.restype = ctypes.POINTER( NFC_DEVICE )  
            self.device = self.lib.nfc_open( context.context, connstring )
            
            if self.device == None:
                raise NfcError()
                  
    def close(self):
        '''
        Close from a NFC device.
        Initiator's selected tag is closed and the device, including allocated nfc_device struct, is released.
        '''
        self.lib.nfc_close(self.device)
        self.device = None
    
    def abortCommand(self):
        '''
        Abort current running command.
        
        Raises:
            NfcError: When LibNfc do not returns NFC_SUCCESS
        '''
        code = self.lib.nfc_abort_command(self.device)
        
        if code != NfcError.NFC_SUCCESS:
            raise NfcError(code)
        
    def idle(self):
        '''
        Turn NFC device in idle mode.
        
        Raises:
            NfcError: When LibNfc do not returns NFC_SUCCESS
        '''
        
        code = self.lib.nfc_idle(self.device)
        
        if code != NfcError.NFC_SUCCESS:
            raise NfcError(code)
        
    def listDevices(self, context=None, connstrings=None ):
        '''
            Scan for discoverable supported devices (ie. only available for some drivers)
            
            Args:
                context (NfcContext, optional): The context object to operate on. Defaults to None.
                connstrings (): List of nfc_connstring.
            
            Returns:
                int: Returns the number of devices found.
            
        '''
        raise NotImplementedError





