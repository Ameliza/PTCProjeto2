#!/usr/bin/env python3

from cliente import Cliente

if __name__ == '__main__':

    print("*** LOGIN ***\n")
    login = input("Login: ")
    senha = input("Senha: ")

    print("O usuário informado foi: %s, e a senha digitada foi: %s" %(login, senha))

    cliente = Cliente(login, senha)
    cliente.authenticate()
    