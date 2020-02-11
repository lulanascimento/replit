from collections import Counter
from datetime import datetime
import json



idcontador = Counter()
idcontador = 1

sair = str(input(" X para fechar o programa ou enter para continuar "))
while( sair == "c" ):

    cadastro = dict()
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
    sair = str(input(" X para fechar o programa ou enter para continuar "))

else:
    print("O usuario digitou x ")
    print(cadastro)
#print(sair)

