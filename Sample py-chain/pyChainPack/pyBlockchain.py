#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:31:39 2019

@author: beehive
"""

import datetime
import hashlib

#-------------CLASSES-------------#
class Block:
    blockNo = 0
    data = None
    nxt = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + \
                            "\nBlockNo: " + str(self.blockNo) + \
                            "\nBlock Data: " + str(self.data) + \
                            "\nHashes: " + str(self.nonce) + \
                            "\n--------------"

class Blockchain:

    diff = 15
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("genesis")
    lnklst = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.nxt = block
        self.block = self.block.nxt

    def powork(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

mychain = Blockchain()