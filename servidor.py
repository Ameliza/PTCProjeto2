#!/usr/bin/env python3

import sys
from socket import*
import provaonline_pb2
from api import API

usuario = ["aluno"]
senha = ["aluno"]
token = None

def checklogin(msg):
    print("LOGIN")
    # verifica se pode autenticar ...
    if msg.login == usuario[0] and msg.senha == senha[0]:
        global token
        token = '378rbf9sd'
        return API.acklogin(token)
    else:
        return API.acklogin('000000000')

def reqprova():
    print("REQPROVA")

def reqresp():
    print("REQRESP")

def reqresultado():
    print("REQRESULTADO")

def logout(msg):
    print("LOGOUT")
    global token
    token = None

if __name__ == '__main__':
    
    s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    s.bind(('0.0.0.0', 8888))
    s.listen()  # espera conexões na porta

    while True:
        print('Esperando conexão...')
        con, addr = s.accept()
        data = con.recv(1024)

        msg,des = API.mensagem(data)
        if des=='login': # se for mensagem de login
            data = checklogin(msg)
            con.send(data)

        elif des=='reqprova':
            reqprova()
            
        elif des=='reqresp':
            reqresp()
            
        elif des=='reqresultado':
            reqresultado()
            
        elif des=='logout':
            logout(msg)

        print("token: ", token)
    