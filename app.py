# Bibliotecas
from flask import Flask, jsonify, request, render_template

# ----------------------------------- FLASK -----------------------------------
app = Flask(__name__, static_folder=None, template_folder='templates')

# Funcionalidades / Endpoints
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/intercom', methods=['GET', 'POST', 'DELETE'])
def intercom():
    # Ler o arquivo TXT
    with open('IDs_de_Conversa.txt', 'r') as arquivo:
      ids_atuais = arquivo.read()

    # handle the POST request
    if request.method == 'POST':
        add_id = request.args.get('id')
        add_id = ' ' + str(add_id)
        with open('IDs_de_Conversa.txt', 'a') as arquivo:
          arquivo.write(add_id)
        with open('IDs_de_Conversa.txt', 'r') as arquivo:
          ids_atuais = arquivo.read()
        resposta = {'conversas_abertas': ids_atuais}
        return jsonify(resposta)

    # handle the DELETE request
    if request.method == 'DELETE':
        del_id = request.args.get('id')
        del_id = ' ' + str(del_id)
        ids_atuais = ids_atuais.replace(del_id, "")
        with open('IDs_de_Conversa.txt', 'w') as arquivo:
          arquivo.write(ids_atuais)
        resposta = {'conversas_abertas': ids_atuais}
        return jsonify(resposta)

    # otherwise handle the GET request
    count = len(ids_atuais.split())
    resposta = {'total_count': count, 'conversas_abertas': ids_atuais}
    return jsonify(resposta)


# References:
#https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-pt
#https://www.hashtagtreinamentos.com/trabalhar-com-arquivos-de-texto-python?gclid=Cj0KCQiA2sqOBhCGARIsAPuPK0jDqMfAq_u6YdY65X_Rs4lvRJNnLyo_oiPUER-ZKddaI5CiRNI7AroaAvfYEALw_wcB
#https://www.treinaweb.com.br/blog/retornando-paginas-html-em-requisicoes-flask
#https://flask-httpauth.readthedocs.io/en/latest/

#import requests
#import json
#import csv
#import pandas as pd
#import gdown
#import oauth2client #import service_account
#from google.cloud import storage
#import gspread
#import df2gspread as d2g
#from pydrive.drive import GoogleDrive
#from df2gspread import df2gspread as d2g
#from google.colab import drive
#import os
#from google.cloud import bigquery
#from google.oauth2 import service_account
#from datetime import date
#from datetime import datetime
