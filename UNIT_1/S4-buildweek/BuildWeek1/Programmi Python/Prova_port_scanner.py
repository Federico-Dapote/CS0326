import socket

target = input("Inserisci l'ip: ") #chiedo all'utente l'ip
port_range = input("Range di porte per lo scan[0-200]: ") #chiedo all'utente il range di porte

port_low = int(port_range.split('-') [0])
port_high = int(port_range.split('-') [1])
print(f'Scansionando {target} da porta {port_low} a {port_high}')

for port in range(port_low, port_high + 1): #fai un ciclo for per trovare la porta nel range, ho messo +1 nella porta high perchè non avrebbe incluso l'ultima porta
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #apro un socket per verificare se c'è una porta aperta
    s.settimeout(0.1)
    status = s.connect_ex((target, port))
    if status == 0:
        print(f'{port}- OPEN')
    else:
        print(f'{port} - CLOSED')
    s.close()