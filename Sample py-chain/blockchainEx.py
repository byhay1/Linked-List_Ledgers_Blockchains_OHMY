#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:30:09 2019

@author: beehive
"""

blockchain = []
        
def last_value_bc(): 
    return blockchain[-1]

def value_add(trans_amt, trans_last=['genesis']): 
    blockchain.append([trans_last,trans_amt])

def user_input(): 
    trans_amt = input("please input your transaction: ")
    return trans_amt

value_add(user_input())
value_add(user_input(), last_value_bc())
value_add(user_input(), last_value_bc())

if __name__ == '__main__': 
    print(blockchain)