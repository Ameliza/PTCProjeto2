#!/usr/bin/python3
 
import sys,time
import provaonline_pb2

auth = provaonline_pb2.LOGIN()
auth.login = 'Ameliza'
auth.senha = '1234'

#msg = provaonline_pb2.MENSAGEM()
# msg.login.login = 'Ameliza'
# msg.login.senha = '12345'
# msg.logout.token = 'basi7saxnsxn9as'

data = auth.SerializeToString()

print('Mensagem codificada:', data)

copia = provaonline_pb2.LOGIN()
copia.ParseFromString(data)
 
print('Mensagem decodificada:')
print('Login:', copia.login)
print('Senha:', copia.senha)
# print('Token Logout:', copia.logout.token)

###############################################

ackresultado = provaonline_pb2.ACK_REQ_RESULTADO()
ackresultado.id_prova = '463467'
ackresultado.nota = 10
questao1 = ackresultado.questoes.add() # tenho que fazer isso por causa do repeated
questao1.questao = 1
questao1.pontos = 2
questao2 = ackresultado.questoes.add()
questao2.questao = 2
questao2.pontos = 4

data1 = ackresultado.SerializeToString()
print('Mensagem codificada:', data1)

copia1 = provaonline_pb2.ACK_REQ_RESULTADO()
copia1.ParseFromString(data1)
 
print('Mensagem decodificada:')
print('ID Prova:', copia1.id_prova)
print('Nota Prova:', copia1.nota)
for RESULTADO in copia1.questoes:
    print('Questão: ', RESULTADO.questao)
    print('Pontos: ', RESULTADO.pontos)
    
###############################################
acklogin = provaonline_pb2.ACK_LOGIN()
acklogin.token = '378rbf9sd'
acklogin.status.codigo = 3627 # creio que possa ser assim por causa do required
acklogin.status.descricao = 'NÃO ESTÁ NO BANCO DE DADOS'

data2 = acklogin.SerializeToString()
print('Mensagem codificada:', data2)

copia2 = provaonline_pb2.ACK_LOGIN()
copia2.ParseFromString(data2)

print('Mensagem decodificada:')
print('ID Prova:', copia2.token)
print('Código Status: ', copia2.status.codigo)
print('Descrição Status: ', copia2.status.descricao)
