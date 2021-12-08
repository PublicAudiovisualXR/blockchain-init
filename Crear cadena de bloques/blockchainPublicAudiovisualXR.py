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
        self.Created_block(proof = 1, previous_hash = '0')

# Parte 2 - Minado de un bloque  de la cadena