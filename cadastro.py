from collections import Counter
from datetime import datetime
import json

cadastro = dict()
idcontador = Counter()
idcontador = 1
#datah = datetime.datetime.now()


cadastro['matricula'] = idcontador + 3
cadastro['nome'] = str(input("Nome do Funcionario: "))
cadastro['nascimento'] = int(input("Ano de Nascimento: "))
cadastro['ctps'] = int(input("Digite o numero da carteira: "))
cadastro['salario'] = float(input("Digite o Salario: R$ "))
cadastro['contratacao'] = int(input("Ano de Contratacao: "))
cadastro['cidade'] = str(input("Cidade Natal: "))
cadastro['estado'] = str(input("Estado de Nascimento: "))
json = json.dumps(cadastro)
f = open("Cadastrados.json","w")
f.write(json)
f.close()

print(cadastro)

