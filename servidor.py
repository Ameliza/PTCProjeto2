#!/usr/bin/env python3

import sys
from socket import*
import provaonline_pb2

LOGIN_INCORRETO = 111
LOGIN_APROVADO = 222

def checklogin():
    acklogin = provaonline_pb2.ACK_LOGIN()
    # verifica se está ok e envia mensagem de resposta
    check = True
    if check:
        acklogin.token = '378rbf9sd' # fazer modo aleatório
        acklogin.status.codigo = LOGIN_APROVADO
        acklogin.status.descricao = 'LOGIN APROVADO'
    else:
        acklogin.status.codigo = LOGIN_INCORRETO
        acklogin.status.descricao = 'LOGIN INCORRETO'

    data = acklogin.SerializeToString()
    # print('Mensagem codificada:', data)

    con.send(data)

    con.shutdown(SHUT_RDWR)

def logout():
    print('LOGOUT')

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    s.bind(('0.0.0.0', 8888))
    s.listen()                  # espera conexões na porta
    print('Esperando conexão...')
    # while True:
    con, addr = s.accept()
    dados = con.recv(1024)

    copia = provaonline_pb2.MENSAGEM()
    copia.ParseFromString(dados)
    print('Mensagem chegou no servidor:\n', copia)

    if copia.HasField('login'): # se for mensagem de login
        checklogin()
    elif copia.HasField('logout'):
        logout()
    copia = provaonline_pb2.LOGIN()
    copia.ParseFromString(dados)
    print('Mensagem chegou no servidor:\n', copia)
    