#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:43:11 2019

@author: beehive
"""
#---------------------
import pyChainPack.pyBlockchain as pyc
from pyChainPack.pyBlockchain import Block

#-------------INITIATE-------------#
if __name__ == '__main__': 
    for n in range(10):
        pyc.mychain.powork(Block("Block " + str(n+1)))
    
    while pyc.mychain.head != None:
        print(pyc.mychain.head)
        pyc.mychain.head = pyc.mychain.head.nxt