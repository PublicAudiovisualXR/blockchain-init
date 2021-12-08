# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:00:05 2021

@author: Jordi_Martos_by_PublicAudiovisual_XR
"""

# Módulo 1 Crear una cadena de bloques Blockchain

# Para Instalar:
# Flask==1.1.2: pip install Flask==1.1.2
# Cliente HTTP Postman: https://www.getpostman.com/

# Importar las librerías
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Parte 1 - Crear la cadena de bloques
class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {'index' : len(self.chain)+1,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'previous_hash' : previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    

# Parte 2 - Minado de un bloque de la cadena