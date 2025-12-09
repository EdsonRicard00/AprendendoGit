# vamos tentar descobrir ips de sites 
# socket - cominicação entre maquinas

import socket
site = input('Digite o nome do site - ex google.com')

try:
    ip = socket.gethostbyname(site)
    #tudo na internet tem um hostname 
    print(ip)
except socket.gaierror:
    #se não funcionar ele me diz o error 
    print('Deu error')