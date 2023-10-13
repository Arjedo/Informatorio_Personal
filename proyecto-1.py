# El juego debe tener una lista de palabras predefinidas de las cuales se
# elige una palabra aleatoriamente para que el jugador adivine.
from random import randint

palabras = ["messi", "casa", "auto", "maradona", "river", "bicicleta"]
indice_palabras_max = len(palabras) - 1
indice_aleatorio = randint(0, indice_palabras_max)#elige un numero al azar entre 0 y 5, que es el indice de cada palabra en la lista palabras

palabra_aleatoria = palabras[indice_aleatorio] # guarda la palabra aleatoria

# El jugador tiene un número limitado de intentos para adivinar la palabra
# (por ejemplo, 6 intentos).
intentos = 6

# Debe mostrar las letras adivinadas y las letras incorrectas.
correctas = []
incorrectas = []
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
palabra_secreta = ['?'] * len(palabra_aleatoria)
print(palabra_secreta)
print(palabra_aleatoria)
# El juego debe verificar si la letra ingresada por el jugador está en la
# palabra secreta y actualizar el estado del juego en consecuencia.

#banderas para salir del bucle y determinar si gano o no el juego
juego_terminado = False
gano_juego = False
perdio_juego = False

print("\t INICIAMOS EL JUEGO")
while not juego_terminado:
    
    letra_ingresada = input("Por favor ingrese una letra: ")

    ind = 0
    existe_letra = False
    #compara la letra ingresada con cada letra de la palabra secreta, si esta la coloca en el indice que se ecnontro
    for letra in palabra_aleatoria: # messi
        if letra == letra_ingresada:
            existe_letra = True
            palabra_secreta[ind] = letra_ingresada

        ind += 1

    if existe_letra:
        correctas.append(letra_ingresada)
        if  "?" not in palabra_secreta:
            juego_terminado = True
            gano_juego = True
    else:
        incorrectas.append(letra_ingresada)
        intentos -= 1
        if intentos == 0:
            juego_terminado = True
            perdio_juego = True

    #letras.remove(letra_ingresada)
    print(palabra_secreta)
    print(f"Letras correctas: {correctas}")
    print(f"Letras incorrectas: {incorrectas}")
    print(f"Intentos restantes: {intentos} \n\n")

if gano_juego:
    print("FELICIDADES! HAS ADIVINADO LA PALABRA")

if perdio_juego:
    print("SUERTE LA PROXIMA! NO HAS ADIVINADO LA PALABRA")