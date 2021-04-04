#!/usr/bin/env python3

import sys
from socket import*
import provaonline_pb2
from api import API



def checklogin():
    
    # verifica se pode autenticar ...
    
    # se tudo OK
    return API.ack_login('378rbf9sd')

def logout():
    print('LOGOUT')

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    s.bind(('0.0.0.0', 8888))
    s.listen()                  # espera conexões na porta
    print('Esperando conexão...')
    # while True:
    con, addr = s.accept()
    data = con.recv(1024)

    msg,des = API.mensagem(data)
    if des=='login': # se for mensagem de login
        data = checklogin()
        con.send(data)
        con.shutdown(SHUT_RDWR)
    elif des=='logout':
        pass
   
    copia = provaonline_pb2.LOGIN()
    copia.ParseFromString(data)
    print('Mensagem chegou no servidor:\n', copia)
    