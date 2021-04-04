#!/usr/bin/env python3

import sys
from socket import*
import provaonline_pb2
from api_application import API_Application

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
        data = API_Application.authenticate(self.usuario, self.senha)

        print('Mensagem codificada:', data)

        self.s.send(data) # envia dados pelo socket

        resposta = self.s.recv(1024)
        acklogin = provaonline_pb2.ACK_LOGIN()
        acklogin.ParseFromString(resposta)
        print('Resposta servidor:\n', acklogin)

        self.s.shutdown(SHUT_RDWR) # como receber mensagem de volta do servidor?

    def request_test(self):
        pass

    def send_replies(self): 
        pass

    def request_result(self):
        pass

    def logout(self):
        pass