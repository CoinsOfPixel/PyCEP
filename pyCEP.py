import json
import requests
import urllib2

print('Qual o CEP que você deseja consultar? ')
cep = int(input())
url = 'http://correiosapi.apphb.com/cep/' + str(cep)
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

print('Os dados para o cep: ' + str(cep) + ' sao: ' + 'Estado: ' + data['estado'],
                                                     'Cidade: ' + data['cidade'],
                                                     'Bairro: ' + data['bairro'],
                                                     'Rua: ' + data['logradouro'])
