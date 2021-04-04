#!/usr/bin/env python3

import sys
from socket import*
import provaonline_pb2
from api import API

class Cliente():
    def __init__(self, login, senha):
        self.usuario = login
        self.senha = senha
        self.token = ''

        # Cria conexão por socket
        self.s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
        self.s.bind(('0.0.0.0', 0))
        self.s.connect(('127.0.0.1', 8888)) # passar IP de destino por argumento de linha

    def close(self):
        self.s.shutdown(SHUT_RDWR) # como receber mensagem de volta do servidor?

    def login(self):
        data = API.login(self.usuario, self.senha)
        print('Mensagem codificada:', data)
        self.s.send(data) # envia dados pelo socket

        resp = self.s.recv(1024)
        msg,des = API.mensagem(resp)
        if des=='acklogin': # se for mensagem de acklogin
            print('Resposta servidor:\n', msg)
            print("token: ",msg.token)
            self.token = msg.token

    
    def logout(self):
        data = API.logout(self.token)
        print('Mensagem codificada:', data)
        self.s.send(data) # envia dados pelo socket

        # resp = self.s.recv(1024)
        # msg,des = API.mensagem(resp)
        # if des=='acklogin': # se for mensagem de acklogin
        #     print('Resposta servidor:\n', msg)
        #     print("token: ",msg.token)
        #     self.token = msg.token