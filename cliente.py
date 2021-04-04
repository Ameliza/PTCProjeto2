#!/usr/bin/env python3

import sys
from socket import*
import provaonline_pb2

class Cliente():
    def __init__(self, login, senha):
        self.usuario = login
        self.senha = senha
        self.token = ''

        # Cria conexão por socket
        self.s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
        self.s.bind(('0.0.0.0', 0))
        self.s.connect(('127.0.0.1', 8888)) # passar IP de destino por argumento de linha

    def authenticate(self):
        auth = provaonline_pb2.LOGIN()
        auth.login = self.usuario
        auth.senha = self.senha

        data = auth.SerializeToString()
        print('Mensagem codificada:', data)

        self.s.send(data) # envia dados pelo socket

        resposta = self.s.recv(1024)
        acklogin = provaonline_pb2.ACK_LOGIN()
        acklogin.ParseFromString(resposta)
        print('Resposta servidor:\n', acklogin)

        self.s.shutdown(SHUT_RDWR) # como receber mensagem de volta do servidor?
