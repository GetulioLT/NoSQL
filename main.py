import requests, json

link = "https://python-in-c6d5c-default-rtdb.firebaseio.com/"

#dados = {"Nome":"Getulio", "Serie":"Sexto","Idade":22}

'''requisicao = requests.post(f"{link}/Alunos/0001/.json", data=dados)

print(requisicao)
print(requisicao.text)'''

'''------------------------------------------------------------------'''

'''requisicao = requests.post(f"{link}/Alunos/.json", data=json.dumps(dados))

print(requisicao)
print(requisicao.text)'''


'''-----------------------------'''

'''dados = {"Nome":"Carlos", "Serie":"quinta","Idade":21}

requisicao = requests.patch(f"{link}/Alunos/-NJA8dLmyrtZjXvsNWBf/.json", data=json.dumps(dados))

print(requisicao)
print(requisicao.text)'''

'''------------------------------'''

'''requisicao = requests.get(f"{link}/.json")

print(requisicao)
#print(requisicao.text)

for i in requisicao.json():
    for j in requisicao.json()[i]:
        print(j, requisicao.json()[i][j])'''

'''----------------------------------------'''

requisicao = requests.delete(f"{link}/-NJA8ayfSi6LuserL2Yy/.json")

print(requisicao)
print(requisicao.text)