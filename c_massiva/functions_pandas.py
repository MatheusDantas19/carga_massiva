import pandas as pd
import numpy as np
import random
from django.shortcuts import redirect


def gerarCargaMassiva(file,user):
    try:
        rel = pd.read_csv(file, encoding="uft-8")

    except IOError as e:
        print("Erro ao ler o arquivo csv")
        return 0

    rel.iloc[:, 2] = rel.iloc[:, 2].replace('F', 'Feminino')
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

    carga['Tipo de usuário'] = 'Estudantes'
    carga['Grau'] = rel.iloc[:, 4]
    carga['Turma'] = rel.iloc[:, 3]

    carga['Senha'] = 1
    carga['Identificador'] = 0

    carga.fillna('')

    carga.to_csv('c_massiva/uploads/'+user+'/cargaGerada2.csv', index=False)

    return 1