import pandas as pd
import numpy as np
import random
from django.shortcuts import redirect


def gerarCargaMassiva(file, user, language):
    try:
        rel = pd.read_csv(file, encoding="uft-8")

    except IOError as e:
        print("Erro ao ler o arquivo csv")
        return 0

    if language == 'pt':
        rel.iloc[:, 2] = rel.iloc[:, 2].replace('F', 'Feminino')
        rel.iloc[:, 2] = rel.iloc[:, 2].replace('M', 'Masculino')
    else:
        rel.iloc[:, 2] = rel.iloc[:, 2].replace('F', 'Femenino')
        rel.iloc[:, 2] = rel.iloc[:, 2].replace('M', 'Masculino')



    carga = pd.DataFrame(
        columns=['Identificador', 'Primeiro Nome', 'Sobrenome', 'Usuario', 'Data de Nascimento', 'Gênero',
                 'Email', 'Tipo de usuário', 'Grau', 'Turma', 'Organização', 'Senha',
                 'Desativado', 'Motivo'])

    carga['Primeiro Nome'] = rel.iloc[:, 0].apply(lambda x: x.split(' ')[0].capitalize())
    carga['Sobrenome'] = rel.iloc[:, 0].apply(lambda x: x.split(' ')[-1].capitalize())
    carga['Usuario'] = rel.iloc[:, 0].apply(lambda x: x.split(' ')[0].lower() + str(random.randint(1, 99)))

    carga['Data de Nascimento'] = rel.iloc[:, 1].apply(lambda x: x.replace('/', '-'))
    carga['Gênero'] = rel.iloc[:, 2]

    carga['Tipo de usuário'] = 'Estudantes' if language == 'pt' else 'Estudiantes'
    carga['Grau'] = rel.iloc[:, 4]
    carga['Turma'] = rel.iloc[:, 3]

    carga['Senha'] = 1
    carga['Identificador'] = 0

    carga.fillna('')

    carga.to_csv('c_massiva/uploads/'+user+'/cargaGerada.csv', index=False)

    return 1

def gerarCargaMassivaGenero(file, user, language):
    try:
        rel = pd.read_csv(file, encoding="uft-8")
    except IOError as e:
        print("Erro ao ler o arquivo csv")
        return 0

    banco = pd.read_csv('static/banco.csv', encoding='utf-8')


    carga = pd.DataFrame(
        columns=['Identificador', 'Primeiro Nome', 'Sobrenome', 'Usuario', 'Data de Nascimento', 'Gênero',
                 'Email', 'Tipo de usuário', 'Grau', 'Turma', 'Organização', 'Senha',
                 'Desativado', 'Motivo'])

    carga['Primeiro Nome'] = rel.iloc[:, 0].apply(lambda x: x.split(' ')[0].capitalize())
    carga['Sobrenome'] = rel.iloc[:, 0].apply(lambda x: x.split(' ')[-1].capitalize())
    carga['Usuario'] = rel.iloc[:, 0].apply(lambda x: x.split(' ')[0].lower() + str(random.randint(1, 99)))
    carga['Data de Nascimento'] = rel.iloc[:, 1].apply(lambda x: x.replace('/', '-'))

    carga['Tipo de usuário'] = 'Estudantes' if language == 'pt' else 'Estudiantes'
    carga['Grau'] = rel.iloc[:, 4]
    carga['Turma'] = rel.iloc[:, 3]

    carga['Senha'] = 1
    carga['Identificador'] = 0

    carga.fillna('')

    for i in range(len(carga)):
        for j in range(len(banco)):
            if carga['Primeiro Nome'][i] == banco['Nome'][j]:
                carga['Gênero'][i] = banco['Sexo'][j]


    carga.to_csv('c_massiva/uploads/'+user+'/cargaGerada.csv', index=False)

    return 1


def dividirCarga(file, user):
    try:
        carga = pd.read_csv(file, encoding="uft-8")

    except IOError as e:
        print("Erro ao ler o arquivo csv")
        return 0


    carga.loc[carga[carga.columns[8]] == 1].to_csv('c_massiva/uploads/'+user+'/1ano.csv', index=False)
    carga.loc[carga[carga.columns[8]] == 2].to_csv('c_massiva/uploads/'+user+'/2ano.csv', index=False)
    carga.loc[carga[carga.columns[8]] == 3].to_csv('c_massiva/uploads/'+user+'/3ano.csv', index=False)
    carga.loc[carga[carga.columns[8]] == 4].to_csv('c_massiva/uploads/'+user+'/4ano.csv', index=False)
    carga.loc[carga[carga.columns[8]] == 5].to_csv('c_massiva/uploads/'+user+'/5ano.csv', index=False)

    carga.loc[(carga[carga.columns[8]] != 1) & (carga[carga.columns[8]] != 2)
                    & (carga[carga.columns[8]] != 3) & (carga[carga.columns[8]] != 4)
                    & (carga[carga.columns[8]] != 5)].to_csv('c_massiva/uploads/'+user+'/Outros.csv', index=False)

    return 1

def juntarCarga(file, user):

    try:
        combined_csv = pd.concat([pd.read_csv(f, encoding='utf-8') for f in file])

    except IOError as e:
        print("Erro ao ler o arquivo csv")
        return 0

    combined_csv.to_csv('c_massiva/uploads/'+user+'/carga_combinada.csv', index=False, encoding='utf-8-sig')
    return 1