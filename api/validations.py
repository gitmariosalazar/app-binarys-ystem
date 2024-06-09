# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:05:07 2024

@author: Mario
"""

import re

def isValid(number, index):
    p=[{
        "id": 0, "base": 0, "pattern": r"^-?\d+(\.\d+)?$", "name": "decimal", "group_value": len(number)
        }, {
        "id": 1, "base": 2, "pattern": r"^[01]+$", "name": "binary", "group_value": 0
        }, {
        "id": 2, "base": 8, "pattern": r"^[0-7]+$","name": "octal", "group_value": 3
        },{
        "id": 3, "base": 16, "pattern": r"^[0-9A-Fa-f]+$","name": "hexadecimal", "group_value": 4
        }]
    regex = re.compile(p[index].get("pattern"))
    return bool(regex.match(number)), p[index]

def getQuantity(number, base):
    p=[{
        "id": 0, "base": 0, "pattern": r"^-?\d+(\.\d+)?$", "name": "decimal", "group_value": len(number)
        }, {
        "id": 1, "base": 2, "pattern": r"^[01]+$", "name": "binary", "group_value": 0
        }, {
        "id": 2, "base": 8, "pattern": r"^[0-7]+$","name": "octal", "group_value": 3
        },{
        "id": 3, "base": 16, "pattern": r"^[0-9A-Fa-f]+$","name": "hexadecimal", "group_value": 4
        }]
    for item in p:
        if(item['base']==base):
            return item['base']==base, item
    return None


def getValuesDecimal(hexadecimal):
    hex_to_dec = {
        "A": "10", "a": "10",
        "B": "11", "b": "11",
        "C": "12", "c": "12",
        "D": "13", "d": "13",
        "E": "14", "e": "14",
        "F": "15", "f": "15"
    }
    return hex_to_dec.get(hexadecimal, hexadecimal), hexadecimal

def getValueHexadecimal(decimal):
    array = [{"number": 10, "word": "A"},{"number": 11, "word": "B"},{"number": 12, "word": "C"},{"number": 13, "word": "D"},{"number": 14, "word": "E"},{"number": 15, "word": "F"}]
    resp=decimal
    for item in array:
        if(str(item['number']) == decimal):
            return item['word']
    return resp