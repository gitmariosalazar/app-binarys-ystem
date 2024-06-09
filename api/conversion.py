# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:03:33 2024

@author: Mario
"""

import validations

def DecimalToOther(to,decimal):
    sign, number = getSignAndNumber(decimal)
    if(to==0 and validations.isValid(number, 0)[0]):
        return sign+number, decimal
    elif(validations.isValid(number, 0)[0]):
        resp=""
        div = int(number)
        cociente = 0
        while(div!=-1 and div!=0):
            cociente = div % to
            div = div//to
            resp = validations.getValueHexadecimal(str(cociente))+resp
        return sign+resp, decimal
    return "The number is not correct!", decimal


def Groupby(cadena, quantity):
    resultado = []
    for i in range(len(cadena)-1, -1, -quantity):
        resultado.append(cadena[max(0, i-quantity+1):i+1])
    return resultado


def BinaryToOther(to, binary_number):
    sign, number = getSignAndNumber(binary_number)
    group_value = validations.getQuantity(number, to)[1].get('group_value')
    if (to==2 and validations.isValid(number, 1)[0]):
        return sign+number, binary_number
    r = ""
    if(validations.isValid(number, 1)[0]):
        group = (Groupby(number, group_value))
        for item in group:
            resp = ""
            aux = 0
            i  = len(item)-1
            for index in range(len(item)):
                aux += (2**i) * int(item[index])
                resp = ""+str(validations.getValueHexadecimal(str(aux)))
                i=i-1
            r = resp + r
        return sign+r, binary_number
    return 'The number is not correct!', binary_number


def Convert(to, n):
    resp = ""
    sign, number = getSignAndNumber(n)
    validate = validations.isValid(number, to)
    a = [0,2,8,16]
    if(validate[0]):
        aux = 0
        i = len(number)-1
        for index in range(len(number)):
            aux = aux + int(a[to]**index)*(int(validations.getValuesDecimal(number[i])[0]))
            resp = "" + str(aux)
            i=i-1
        return sign+resp
    return sign+resp



def OctalToOther(to, number):
    decimal = Convert(2, number)
    return DecimalToOther(to, decimal)

def HexadecimalToOther(to, number):
    decimal = Convert(3, number)
    return DecimalToOther(to, decimal)

def getSignAndNumber(number):
    if(number[0] == '-'):
        return number[0], number[1:]
    return '', number



print(DecimalToOther(0,"1234567a")) 
print(DecimalToOther(2,"1234567")) 
print(DecimalToOther(8,"1234567")) 
print(DecimalToOther(16,"1234567"))
print()
print(BinaryToOther(0, "-100101101011010000111"))
print(BinaryToOther(2, "-100101101011010000111"))
print(BinaryToOther(8, "-100101101011010000111"))
print(BinaryToOther(16, "-100101101011010000111"))
print()
print(OctalToOther(0, "4553207"))
print(OctalToOther(2, "4553207"))
print(OctalToOther(8, "4553207"))
print(OctalToOther(16, "4553207"))
print()
print(HexadecimalToOther(0, "12D687"))
print(HexadecimalToOther(2, "12D687"))
print(HexadecimalToOther(8, "12D687"))
print(HexadecimalToOther(16, "12D687"))
