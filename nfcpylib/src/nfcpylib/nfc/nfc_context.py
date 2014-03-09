'''
Created on Feb 12, 2014

@author: ingenious debilitation
@summary: Python ctypes-based wrapper for nfc_context structure. Original definition is in file nfc_internal.h
@see: http://www.libnfc.org/api/nfc-internal_8h_source.html
@see: http://www.libnfc.org/api/group__lib.html
@todo: register driver method

'''

from ctypes import Structure, c_bool, c_uint32, CDLL, pointer, byref
from src.nfcpylib.nfc_internal.nfc_user_defined_device import NFC_USER_DEFINED_DEVICE
from src.nfcpylib.types.constants import MAX_USER_DEFINED_DEVICES


class NFC_CONTEXT(Structure):
    
    _fields_ = [
                ( 'allow_autoscan', c_bool ),                   # bool allow_autoscan;
                ( 'allow_intrusive_scan', c_bool ),             # bool allow_intrusive_scan;
                ( 'log_level', c_uint32),                       # uint32_t  log_level;
                ('user_defined_devices', NFC_USER_DEFINED_DEVICE * MAX_USER_DEFINED_DEVICES),   # struct nfc_user_defined_device user_defined_devices[MAX_USER_DEFINED_DEVICES];
                ('user_defined_device_count', c_uint32 )        # unsigned int user_defined_device_count;
                ]

class NfcContext(object):
    '''
    NfcContext class
    '''
    LIBPATH = "/usr/lib/libnfc.so"
    
    @property
    def context(self):
        return self._context
    
    @context.setter
    def context(self, context):
        self._context = context
        
    @property
    def lib(self):
        return self._lib
    
    @lib.setter
    def lib(self, lib):
        self._lib = lib
    
    def __init__(self, libpath=LIBPATH):
        '''
        Initialize libnfc. This function must be called before calling any other libnfc function.
        
        Args:
            libpath (string, optional): LibNfc library path. Defaults to LIBPATH constant.
        '''   
        try:
            # Open shared library
            self.lib = CDLL(libpath)
        except OSError as e:
            raise e
        else:
            # Create context structure and initialize it
            self.context = pointer( NFC_CONTEXT() )
            self.lib.nfc_init( byref( self.context ) )
         
    def close(self):
        '''
        Deinitialize libnfc. Should be called after closing all open devices and before your application terminates.    
        '''
        self.lib.nfc_exit(self.context)
        self.context = None                 # Garbage collector frees automatically when no reference
    
    def registerDriver(self, driver):
        '''
        Register an NFC device driver with libnfc. This function registers a driver with libnfc, the caller is responsible of 
        managing the lifetime of the driver and make sure that any resources associated with the driver are available after registration.
        
        Args:
            driver (): Pointer to an NFC device driver to be registered.
            
        Returns:
             int: NFC_SUCCESS
        
        Raises:
            NfcError: When LibNfc do not returns NFC_SUCCESS
        '''
        raise NotImplementedError
        
