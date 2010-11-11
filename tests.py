#!/usr/bin/env python
# -*- coding=utf-8 -*-
#        0123456
TELEFONE = '499021'
TELEFONES = ['629701', '349765', '542594', '628307', '695687']


def tem_6_digitos(telefone):
    return len(telefone) == 6

def primeiro_ultimo_iguais(telefone):
    return telefone[0] == telefone[-1]

def tem_numeros_consecutivo(telefone):
    for i, n in enumerate(telefone[:-2]):
        if n == telefone[i + 1]:
             return True
    else:
        return False

def soma_par(telefone):
    soma = 0
    for i in telefone:
        soma += int(i)
    return soma % 2 == 0                    
def processa_lista(telefones):
    lista_procesada = {}


def teste_tem_6_digitos():
    assert tem_6_digitos(TELEFONE) == True
    
def teste_primeiro_ultimo_iguais():
    #testa se o primeiro e ultimo digito sao iguais
    assert primeiro_ultimo_iguais(TELEFONE) == False

def teste_tem_numeros_consecutivo():
    #testa se ha numero consecutivo iguais
    assert tem_numeros_consecutivo(TELEFONE) == True

def teste_soma_par():
    assert soma_par(TELEFONE) == False

def teste_lista():
    assert processa_lista(TELEFONES) == {'629701':False, '349765':True, 
        '542594':False, '628307': True, '695687': False}


