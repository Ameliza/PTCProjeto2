#!/usr/bin/env python3

import sys
import provaonline_pb2

LOGIN_INCORRETO = 111
LOGIN_APROVADO = 222

class API():
    
    def mensagem(data):
        msg = provaonline_pb2.MENSAGEM()
        msg.ParseFromString(data)
        print('Mensagem recebida:\n', msg)

        if msg.HasField('login'):
            l = provaonline_pb2.LOGIN()
            l.login = msg.login.login
            l.senha = msg.login.senha    
            return l,"login"

        elif msg.HasField('logout'):
            l = provaonline_pb2.LOGOUT()
            l.token = msg.logout.token
            return l,"logout"

        elif msg.HasField('acklogin'):
            a = provaonline_pb2.ACK_LOGIN()
            a.token = msg.acklogin.token
            a.status.codigo = msg.acklogin.status.codigo
            a.status.descricao = msg.acklogin.status.descricao
            return a,"acklogin"
            
        elif msg.HasField('reqprova'):
            pass
        elif msg.HasField('ackreqprova'):
            pass
        elif msg.HasField('reqresultado'):
            pass
        elif msg.HasField('ackreqresultado'):
            pass
        elif msg.HasField('reqresp'):
            pass

    def login(usuario, senha):
        m = provaonline_pb2.MENSAGEM()
        m.login.login = usuario
        m.login.senha = senha
        return m.SerializeToString()
    
    
    def ack_login(token):
        m = provaonline_pb2.MENSAGEM()
        m.acklogin.token = token
        m.acklogin.status.codigo = LOGIN_APROVADO
        m.acklogin.status.descricao = 'LOGIN APROVADO'
        return m.SerializeToString()

    
    def logout(token):
        m = provaonline_pb2.MENSAGEM()
        m.logout.token = token

        data = m.SerializeToString()
        return data