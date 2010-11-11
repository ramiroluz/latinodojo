#!/usr/bin/env python
# -*- coding=utf-8 -*-

Telefone=499021

def Tem6Digitos(NTelefone):
    return len(str(NTelefone))==6

def PrimeiroUltimoIguais(NTelefone):
    stelefone = str(NTelefone)
    return stelefone[0] == stelefone[-1]

def test1():
    assert Tem6Digitos(Telefone)==True
    
def test2():
    #testa se o primeiro e ultimo digito sao iguais
    assert PrimeiroUltimoIguais(Telefone)==False

def test3():
    #testa se ha numero consecutivo iguais
    assert NumerosConsecutivo(Telefone)==True
