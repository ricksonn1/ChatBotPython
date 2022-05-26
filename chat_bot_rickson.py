import os

def processar_resposta(resposta, nome):
    if resposta == "1":
        print(f"{os.linesep}{nome.title()} Eu tenho 25 anos!{os.linesep}")
    elif resposta == "2":
        print(f"{os.linesep}{nome.title()}, atualmente estou trabalhando na Riachuelo como assistente administrativo.{os.linesep}")
    elif resposta == "3":
        print(f"{os.linesep}{nome.title()} minha cidade onde nasci é Manaus, mas atualmente moro em Brasilia.{os.linesep}")
    elif resposta == "4":
        print(f"{os.linesep}{nome.title()} sim, sou casado com a Lorena!{os.linesep}")
    elif resposta == "5":
        print(f"{os.linesep}{nome.title()} Estou no 2* semestre de Ciência da computação!{os.linesep}")

    else:
        print("Digite apenas as opções que aparecem na tela!!")

def chat():
    print("*************************************")
    print("Olá, bem vindo ao chat bot do Rickson")
    print("*************************************\n")
    nome = input("Qual o seu nome e sobrenome?: ")
    email = input("Qual seu email?: ")
    telefone = input("Qual seu número de telefone?: ")
    while True:
        resposta = input(f"O que gostaria de saber sobre mim hoje?\n[1] - Minha idade?\n"f"[2] - Onde trabalho?\n[3] - Minha cidade?\n[4] - Sou casado?\n"
                         f"[5] - Qual superior estou cursando?")
        processar_resposta(resposta, nome)

if __name__ == "__main__":
    chat()