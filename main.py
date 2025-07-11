from logica import procesar

print('░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░\n░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░    ░▒▓██▓▒░░▒▓█▓▒░░▒▓█▓▒░\n░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓██▓▒░  ░▒▓████████▓▒░\n░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓██▓▒░    ░▒▓█▓▒░░▒▓█▓▒░\n░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░\n░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░')

print('esta lista para hablar contigo \nescribe salir si deseas terminar la conversación')

while True:
    entrada = input('> ')
    if entrada.lower() == 'salir':
        print('Saliendo del programa...')
        break
    respuesta = procesar(entrada)
    print(f'> {respuesta}')

