#!/usr/bin/env python3

import sys
import provaonline_pb2

class API_Application():
    def authenticate(usuario, senha):
        auth = provaonline_pb2.LOGIN()
        auth.login = usuario
        auth.senha = senha

        data = auth.SerializeToString()
        return data