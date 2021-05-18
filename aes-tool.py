# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:55:49 2019

@author: Administrator
"""
import base64
import binascii
from Crypto.Cipher import AES
from Crypto import Random
import os
import base64
import json

key="1234567890123456"
vi="1234567890123456"

encoding='utf8'

def AES_Encrypt(key, data):
    pad = lambda s: s + (16 - len(s)%16) * chr(16 - len(s)%16)
    data = pad(data)
    cipher = AES.new(key.encode(encoding), AES.MODE_CBC, vi.encode(encoding))
    encryptedbytes = cipher.encrypt(data.encode(encoding))
    return binascii.b2a_hex(encryptedbytes).decode(encoding)


def AES_Decrypt(key, data):
    data = data.encode(encoding)
    encodebytes = binascii.a2b_hex(data)
    # 将加密数据转换位bytes类型数据
    cipher = AES.new(key.encode(encoding), AES.MODE_CBC, vi.encode(encoding))
    text_decrypted = cipher.decrypt(encodebytes)
    unpad = lambda s: s[0:-s[-1]]
    text_decrypted = unpad(text_decrypted)
    # 去补位
    text_decrypted = text_decrypted.decode(encoding)
    return text_decrypted

if __name__=="__main__":
    encoded="b14014e31b789f7ef13dd73a24abd819e29241cf49259dbe65771a2c639853997d1bbde09c475f9c5d181525f0bf327822cfa16b57b56e38da4f8bbb8446ccdf412b4921e617847b3a069ce0eb9a44c2798c37d0aa535a825643f6f4a23329b1038d731d6045f2c87e87bd8c3a497aa6"
    print(AES_Decrypt(key,encoded))
    myEncoded=AES_Encrypt(key,"HELLO WORLD")
    print(myEncoded)
    print(AES_Decrypt(key,myEncoded))