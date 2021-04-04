#!/usr/bin/env python3

from cliente import Cliente

LOGIN = '1'
PROVA = '2'
RESPOSTAS = '3'
RESULTADO = '4'
LOGOUT = '5'

def menu(switch):
    
    print("------ MENU ------")
    print("1 - Login")
    print("2 - Requisição de prova")
    print("3 - Respostas da prova")
    print("4 - Resultado da prova")
    print("5 - Logout")
    option = input(">> ")
    switch[option]()

def login():
    print("****** LOGIN *****\n")
    login = input("Login: ")
    senha = input("Senha: ")
    cliente = Cliente(login, senha)
    cliente.authenticate() 

def prova():
    print("prova")

def respostas():
    print("respostas")

def resultado():
    print("resultado")

def logout():
    print("logout")

if __name__ == '__main__':
    cliente = None
    switch = {
        LOGIN: login,
        PROVA: prova,
        RESPOSTAS: respostas,
        RESULTADO: resultado,
        LOGOUT: logout
    }

    menu(switch)
    