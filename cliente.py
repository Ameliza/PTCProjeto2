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

    def connect(self):
        # Cria conexão por socket
        self.s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
        self.s.bind(('0.0.0.0', 0))
        self.s.connect(('127.0.0.1', 8888)) # passar IP de destino por argumento de linha
        
    def login(self):
        self.connect()
        data = API.login(self.usuario, self.senha)
        print('Mensagem codificada:', data)
        self.s.send(data) # envia dados pelo socket
        ## espera ack
        resp = self.s.recv(1024)
        msg,des = API.mensagem(resp)
        if des=='acklogin': # se for mensagem de acklogin
            print('Resposta servidor:\n', msg)
            print("token: ",msg.token)
            self.token = msg.token
        self.s.shutdown(SHUT_RDWR) # como receber mensagem de volta do servidor?
    
    def reqprova(self, id_prova):
        self.connect()
        data = API.reqprova(self.token, id_prova)
        print('Mensagem codificada:', data)
        self.s.send(data) # envia dados pelo socket
        ## espera ack
        resp = self.s.recv(1024)
        msg,des = API.mensagem(resp)
        if des=='ackreqprova': # se for mensagem de acklogin
            print('Resposta servidor:\n', msg)
        self.s.shutdown(SHUT_RDWR) # como receber mensagem de volta do servidor?
    
    def reqresp(self, token, id_prova, respostas):
        self.connect()
        data = API.reqresp(self.token, id_prova, respostas)
        print('Mensagem codificada:', data)
        self.s.send(data) # envia dados pelo socket
        ## ack??
        self.s.shutdown(SHUT_RDWR) # como receber mensagem de volta do servidor?
    
    def reqresultado(self, token, id_prova):
        self.connect()
        data = API.reqresultado(self.token, id_prova)
        print('Mensagem codificada:', data)
        self.s.send(data) # envia dados pelo socket
        ## espera ack
        resp = self.s.recv(1024)
        msg,des = API.mensagem(resp)
        if des=='ackreqresultado': # se for mensagem de acklogin
            print('Resposta servidor:\n', msg)
        self.s.shutdown(SHUT_RDWR) # como receber mensagem de volta do servidor?
    
    def logout(self):
        self.connect()
        data = API.logout(self.token)
        print('Mensagem codificada:', data)
        self.s.send(data) # envia dados pelo socket
        ## ack??
        self.s.shutdown(SHUT_RDWR) # como receber mensagem de volta do servidor?