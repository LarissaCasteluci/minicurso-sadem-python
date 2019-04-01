"Oi, eu sou o/a fulana. Tenho XX anos e nasci em XXXX. Estou estudando XXXXX XXXXX desde o ano de XXXX. "

nome = input("Qual seu nome?\n").strip() #strip remove espaços no começco e no final da string
                        #rstrip no final
                        #lstrip no começo

sexo = input("Qual seu sexo?\n").strip().lower()

if sexo == "f" or sexo == "feminino":
    artigo = "a"
elif sexo == "m" or sexo == "masculino":
    artigo = "o"
else:
    artigo = ""

resultado = "Oi, eu sou " + nome + "." if artigo == "" else "Oi, eu sou " + " ".join([artigo,nome]) + ". "

ano_nascimento = int(input("Em que ano você nasceu?\n"))

import datetime

ano_atual = datetime.datetime.now().year

cidade_natal = input("Em qual cidade você nasceu?\n").strip()

resultado = resultado + "Tenho " + str(ano_atual -  ano_nascimento) + " anos e nasci em " + cidade_natal + ". "

curso = input("Qual curso você está fazendo na faculdade?\n").strip()

ano_ingresso = input("Em que ano você ingressou no curso de " + curso + "?\n").strip()

resultado = resultado + "Estou cursando " + str(curso) + " desde o ano de " + str(ano_ingresso) + ". "

print(resultado)