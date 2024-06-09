# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:03:00 2024

@author: Mario
"""

from flask import Flask, jsonify, request
from models import conversion, validations

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": 'Pong!'})


@app.route('/decimal/<decimal>', methods=['GET'])
def DecimalToOther(decimal):
    sign, number = conversion.getSignAndNumber(decimal)
    if decimal and validations.isValid(number=number, index=0)[0]:
        return jsonify({
            'message': "Request successfull!",
            'decimal': conversion.DecimalToOther(0, decimal)[0],
            'binary': conversion.DecimalToOther(2, decimal)[0],
            'octal': conversion.DecimalToOther(8, decimal)[0],
            'hexadecimal': conversion.DecimalToOther(16, decimal)[0]
            })
    else:
        return jsonify({
            'message': "Request failed, The decimal number is not correct!"
            })


@app.route('/binary/<binary>', methods=['GET'])
def BinaryToOther(binary):
    sign, number = conversion.getSignAndNumber(binary)
    if binary and validations.isValid(number=number, index=1)[0]:
        return jsonify({
            'message': "Request successfull!",
            'decimal': conversion.BinaryToOther(0, binary_number=binary)[0],
            'binary': conversion.BinaryToOther(2, binary_number=binary)[0],
            'octal': conversion.BinaryToOther(8, binary_number=binary)[0],
            'hexadecimal': conversion.BinaryToOther(16, binary_number=binary)[0]
            })
    else:
        return jsonify({
            'message': "Request failed, The binary number is not correct!"
            })


@app.route('/octal/<octal>', methods=['GET'])
def OctalToOther(octal):
    sign, number = conversion.getSignAndNumber(octal)
    if validations.isValid(number=number, index=2)[0]:
        return jsonify({
            'message': "Request successfull!",
            'decimal': conversion.OctalToOther(0, octal)[0],
            'binary': conversion.OctalToOther(2, octal)[0],
            'octal': conversion.OctalToOther(8, octal)[0],
            'hexadecimal': conversion.OctalToOther(16, octal)[0]
            })
    else:
        return jsonify({
            'message': "Request failed, The octal number is not correct!"
            })


@app.route('/hexadecimal/<hexadecimal>', methods=['GET'])
def HexadecimalToOther(hexadecimal):
    sign, number = conversion.getSignAndNumber(hexadecimal)
    if number and validations.isValid(number=number, index=3)[0]:
        return jsonify({
            'message': "Request successfull!",
            'decimal': conversion.HexadecimalToOther(0, hexadecimal)[0],
            'binary': conversion.HexadecimalToOther(2, hexadecimal)[0],
            'octal': conversion.HexadecimalToOther(8, hexadecimal)[0],
            'hexadecimal': conversion.HexadecimalToOther(16, hexadecimal)[0]
            })
    else:
        return jsonify({
            'message': "Request failed, The hexadecimal number is not correct!"
            })
    

if __name__ == '__main__':
    app.run(debug=True, port=4000)