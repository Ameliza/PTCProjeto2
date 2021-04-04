#!/usr/bin/env python3

import sys
from socket import*
import provaonline_pb2

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    s.bind(('0.0.0.0', 8888))
    print('ok1')
    s.listen()                  # espera conexões na porta
    print('ok2')
    # while True:
    con, addr = s.accept()
    dados = con.recv(1024) # como verificar se o dado é do tipo login?
    copia = provaonline_pb2.LOGIN()
    copia.ParseFromString(dados)
    print('Mensagem chegou no servidor:\n', copia)
    # verifica se está ok e envia mensagem de resposta
    acklogin = provaonline_pb2.ACK_LOGIN()
    acklogin.token = '378rbf9sd'
    acklogin.status.codigo = 3627
    acklogin.status.descricao = 'NÃO ESTÁ NO BANCO DE DADOS'

    data = acklogin.SerializeToString()
    # print('Mensagem codificada:', data)

    con.send(data)

    con.shutdown(SHUT_RDWR)