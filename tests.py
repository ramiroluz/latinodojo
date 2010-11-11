#!/usr/bin/env python
# -*- coding=utf-8 -*-

def Tem6Digitos(NTelefone):
    return len(str(NTelefone))==6

def test1():
    assert Tem6Digitos(499021)==True

