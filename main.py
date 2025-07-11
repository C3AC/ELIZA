from logica import procesar
from checks import estado

print('░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░\n░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░    ░▒▓██▓▒░░▒▓█▓▒░░▒▓█▓▒░\n░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓██▓▒░  ░▒▓████████▓▒░\n░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓██▓▒░    ░▒▓█▓▒░░▒▓█▓▒░\n░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░\n░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░')

print('escribe salir para terminar el programa')

while True:
    entrada = input('> ')
    if entrada.lower() == 'salir':
        print('Saliendo del programa...')
        break
    respuesta = procesar(entrada, estado)
    print(f'> {respuesta}')

