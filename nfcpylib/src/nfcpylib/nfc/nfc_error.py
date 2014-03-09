'''
Created on Feb 21, 2014

@author: ingenious debilitation
'''
class NfcError(Exception):
    NFC_SUCCESS = 0
    NFC_EIO = -1
    NFC_EINVARG = -2
    NFC_EDEVNOTSUPP = -3
    NFC_ENOTSUCHDEV = -4
    NFC_EOVFLOW = -5
    NFC_ETIMEOUT = -6
    NFC_EOPABORTED = -7
    NFC_ENOTIMPL = -8
    NFC_ETGRELEASED = -10
    NFC_ERFTRANS = -20
    NFC_EMFCAUTHFAIL = -30
    NFC_ESOFT = -80
    NFC_ECHIP = -90
    DEFAULT_ERR_CODE = -69
    
    def __init__(self, code):
        self.code = code
        
    def __str__(self):
        return repr( NfcError.errorMessage (self.code ) )
    
    @staticmethod
    def errorMessage(code): # Pythonian switch hack
        return {
            NfcError.NFC_SUCCESS: 'NFC Success',
            NfcError.NFC_EIO: 'NFC IO Error',
            NfcError.NFC_EINVARG: 'NFC_EINVARG',
            NfcError.NFC_EDEVNOTSUPP: 'NFC_EDEVNOTSUPP',
            NfcError.NFC_ENOTSUCHDEV: 'NFC_ENOTSUCHDEV',
            NfcError.NFC_EOVFLOW: 'NFC_EOVFLOW',
            NfcError.NFC_ETIMEOUT: 'NFC_ETIMEOUT',
            NfcError.NFC_EOPABORTED: 'NFC_EOPABORTED',
            NfcError.NFC_ENOTIMPL: 'NFC_ENOTIMPL',
            NfcError.NFC_ETGRELEASED: 'NFC_ETGRELEASED',
            NfcError.NFC_ERFTRANS: 'NFC_ERFTRANS',
            NfcError.NFC_EMFCAUTHFAIL: 'NFC_EMFCAUTHFAIL',
            NfcError.NFC_ESOFT: 'NFC_ESOFT',
            NfcError.NFC_ECHIP: 'NFC_ECHIP',
            NfcError.DEFAULT_ERR_CODE: 'Unknown error'
            }.get(code, NfcError.DEFAULT_ERR_CODE)
            