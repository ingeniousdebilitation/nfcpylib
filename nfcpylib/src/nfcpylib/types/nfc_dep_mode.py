'''
Created on Feb 13, 2014

@author: chainer
'''
from ctypes import c_long
    
class NFC_DEP_MODE(object): # enum hack in Python 2.7
    NDM_UNDEFINED = c_long(0)
    NDM_PASSIVE = c_long(1)
    NDM_ACTIVE = c_long(2)
