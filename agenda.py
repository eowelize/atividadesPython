import keyboard
import time
import os
def EsperarTecla(teclasValidas):
    while True:
        key_pressed = keyboard.read_key()
        if(key_pressed != ""):
            if(len(teclasValidas) ==0):
                return key_pressed
            if(key_pressed in teclasValidas):
                return key_pressed
        time.sleep(0.3)


def SelecionarTipoContatos():
    time.sleep(1)
    print("Selecione o tipo do contato")
    print("0 -> Pessoal")
    print("1 -> Profissional")
    print("2 -> Romantico")
    tipo = EsperarTecla(["0", "1", "2"])
contatos = []

import EsperaTecla

def criarContato(nome, telefone, endereco, tipo):

    contato = {}
    contato["numero"] = len(contatos)
    contato["nome"] = nome
    contato["telefone"] = telefone
    contato["Endereco"] = endereco
    contato["tipo"] = tipo
    return contato

def preencherFormulário():
    print("Agora vamos adicionar um contato novo!")
    Nome = input("Digite o nome do contato!")
    Telefone = input("digite o número do contato:")
    Endereco = input("digite o endereco do contato:")
    print("Selecione o tipo do contato")
    print("0 -> pessoal")
    print("1 -> Profissional")
    print("2 -> Romantico")
    Tipo = EsperaTecla([1,2,3])