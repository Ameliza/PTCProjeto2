#!/usr/bin/env python3

import sys
from socket import*
import provaonline_pb2
from api import API

usuario = ["aluno"]
senha = ["aluno"]
token = None

def checklogin(msg):
    
    # verifica se pode autenticar ...
    if msg.login == usuario[0] and msg.senha == senha[0]:
        global token
        token = '378rbf9sd'
        return API.ack_login(token)
    else:
        return API.ack_login('000000000')

def logout(msg):
    global token
    token = None

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    s.bind(('0.0.0.0', 8888))
    # s.listen()  # espera conexões na porta
    while True:
        print('Esperando conexão...')
        s.listen()  # espera conexões na porta
        con, addr = s.accept()
        data = con.recv(1024)
        print("conectou")

        msg,des = API.mensagem(data)
        if des=='login': # se for mensagem de login
            print("LOGIN")
            data = checklogin(msg)
            con.send(data)
            con.shutdown(SHUT_RDWR)
        elif des=='logout':
            print("LOGOUT")
            logout(msg)

        print("token: ", token)
    