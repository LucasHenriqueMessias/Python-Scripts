"""
Author: Lucas Henrique Messias Gonçalves
Date: september 29th 2022
Function of this code: This Script collect the information of address (like street, Complement, CEP, and others informations of Brazilian's Streets), 
and turns into a json, using the ViaCep's API.
Could be used to collect informations of clients to sales.
"""
import requests

#receiving the request from viacep's API
cep_input = input('Digite o CEP(somente numeros): ') #Input data 
request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input)) #receiving the information from viacep, using cep_input as parameter of consult
request = request.json() #update the information for json

#Data's tratative and print
print('#####################################')
if len(cep_input) != 8:
    print('cep informado diferente de 8')
    exit()
elif 'erro' in request:
    print('cep inexistente')
else:
    print('todas as informacoes: {}'.format(request))
    print('somente endereco: '.format(request['logradouro']))