import pandas as pd
import random
import csv

arquivo = pd.read_csv('dados_clientes.csv')
id_usuarios = arquivo["id"].tolist()
mensagens_ao_usuario = arquivo["nome"].tolist()

def dados_cadastro(id):
    indice = id - 1
    dados = {'Nome': arquivo['nome'][indice], 'Idade': arquivo['idade'][indice], 'E-mail': arquivo['e-mail'][indice],
             'Mensagem': arquivo['mensagem'][indice], }
    return [f'Nome: {dados["Nome"]} - Idade: {dados["Idade"]} - E-mail: {dados["E-mail"]} - Mensagem: '
            f'{dados["Mensagem"]}']

def mensagem_para_usuario(id):
    indice = id-1
    arquivo_mensagem = open('mensagens.txt', 'r')
    mensagens = [msg for msg in arquivo_mensagem]
    mensagem_aleatoria = mensagens[random.randrange(len(mensagens))]
    return f'{arquivo["nome"][indice]} {mensagem_aleatoria}'

user = [user for i in id_usuarios if (user := dados_cadastro(i)) is not None]
mensagens = [mensagem_para_usuario(id) for id in id_usuarios]


for i in range(10):
    with open('dados_clientesI.csv', 'a', newline="", encoding="utf-8") as arq:
        novo_arquivo = csv.writer(arq)
        novo_arquivo.writerow([user[i][0].replace("nan", mensagens[i])])






